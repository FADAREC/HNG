from pysnmp.entity.rfc3413.oneliner import cmdgen # type: ignore

def snmp_get(ip, community, oid):
    cmd_gen = cmdgen.CommandGenerator()
    error_indication, error_status, error_index, var_binds = cmd_gen.getCmd(
        cmdgen.CommunityData(community),
        cmdgen.UdpTransportTarget((ip, 161)),
        oid
    )

    if error_indication:
        return f"SNMP Error: {error_indication}"
    elif error_status:
        return f"SNMP Error: {error_status.prettyPrint()}"
    else:
        return f"{var_binds[0][1]}"

# Example usage
printer_ip = "10.75.2.86"  # Change this
community_string = "public"  # Change if needed

oids = {
    "Device Model": "1.3.6.1.2.1.25.3.2.1.3.1",
    "Total Page Count": "1.3.6.1.2.1.43.10.2.1.4.1.1",
    "Black Toner Level": "1.3.6.1.2.1.43.12.1.1.4.1.1",
    "Printer Status": "1.3.6.1.2.1.25.3.5.1.1.1"
}

for key, oid in oids.items():
    print(f"{key}: {snmp_get(printer_ip, community_string, oid)}")
