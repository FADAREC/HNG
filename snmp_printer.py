import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth
import pandas as pd
from datetime import datetime

USERNAME = "admin"
PASSWORD = "Inv$$prt12"


PRINTERS = {
    "10.75.2.212": "Technology Office",
    "10.75.2.202": "Stockbroking (SecondFloor Color Printer)",
    "10.75.2.208": "Admin (GroundFloor Right Wing)",
    "10.75.2.97": "Fincon Office (ThirdFloor Right-Wing Printer)",
    "10.75.5.201": "OrangeOne Office",
    "10.75.2.205": "Legal Office",
    "10.75.2.206": "HR Printer",
    "10.75.2.214": "GCOO Office",
    }

EXCEL_FILE = "printer_toner_log_backup.xlsx"

def get_toner_levels(ip):
    """Fetches toner levels from printers that require authentication."""
    url = f"http://{ip}/"
    try:
        response = requests.get(url, auth=HTTPBasicAuth(USERNAME, PASSWORD), timeout=5)
        response.raise_for_status()  

        soup = BeautifulSoup(response.text, 'html.parser')

        model_tag = soup.find("title")  
        printer_model = model_tag.text.strip() if model_tag else "Unknown Model"

        toner_levels = {}
        for color in ["Black", "Cyan", "Magenta", "Yellow"]:
            toner_tag = soup.find(string=lambda text: text and color in text)
            if toner_tag:
                toner_value = toner_tag.find_next("td").text.strip()
                toner_levels[color] = toner_value if toner_value else "Empty"
            else:
                toner_levels[color] = "N/A" if color != "Black" else "Empty"

        return printer_model, toner_levels
    except requests.RequestException:
        return None, None  
    
def update_excel():
    """Fetches toner data from all printers & appends to an Excel file."""
    data = []
    today = datetime.now().strftime("%Y-%m-%d")

    for ip, name in PRINTERS.items():
        printer_model, toner_levels = get_toner_levels(ip)
        if printer_model:
            status = "OK"
        else:
            printer_model = "-"
            toner_levels = {"Black": "-", "Cyan": "-", "Magenta": "-", "Yellow": "-"}
            status = "Please manually check"

        data.append([
            today, name, printer_model, ip,
            toner_levels["Black"], toner_levels["Cyan"],
            toner_levels["Magenta"], toner_levels["Yellow"], status
        ])

    df = pd.DataFrame(data, columns=[
        "Date", "Printer Name", "Printer Model", "IP Address",
        "Black Toner", "Cyan Toner", "Magenta Toner", "Yellow Toner", "Status"
    ])

    try:
        existing_df = pd.read_excel(EXCEL_FILE)
        df = pd.concat([existing_df, df], ignore_index=True)
    except FileNotFoundError:
        pass 

    df.to_excel(EXCEL_FILE, index=False)
    print("✅ Toner levels updated!  click on the link to access excelsheet  ")

if __name__ == "__main__":
    update_excel()
