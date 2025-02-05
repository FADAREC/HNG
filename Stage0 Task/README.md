# HNG12 Backend Stage 0 Task

## Overview
This project implements a simple backend API using Python and Flask to return basic user information in JSON format. The API provides the following data:
- Your registered email address.
- The current UTC datetime in ISO 8601 format.
- The URL to the GitHub repository for this project.

## Technology Stack
- **Programming Language**: Python 3.x
- **Framework**: Flask
- **CORS Handling**: Flask-CORS
- **Deployment**: The API is deployed on [render](https://www.render.com/)

## Features
- Public API endpoint that returns basic information in JSON format.
- Dynamic generation of the current date and time in ISO 8601 format (UTC).
- Proper handling of CORS requests to allow access from different origins.

## Setup Instructions

### Prerequisites
Before running the project locally, ensure you have the following:
- Python 3.x installed.
- `pip` (Python package installer) for managing dependencies.

### Steps to Run the Project Locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/FADAREC/HNG.git
   cd HNG

2. **Create Virtual Environment(Optional)**
    ```bash 
    python3 -m venv venv
    source venv/bin/activate  # For macOS/Linux
    source venv/Scripts/activate     # For Windows

3. **Install dependencies** : Incase `requirements.txt` file is not present upon cloning, create one by yourself by running:
    ```bash
    pip install flask flask-cors
    pip freeze > requirements.txt
Then install the dependencies:
    ```bash
    pip install -r requirements.txt

4. **Run the application**
    ```bash
    python app.py

5. **Access the API**
    ```bash
    http://localhost:5000/


### API Documentation
    ## API Documentation
    ### Endpoint: `/api/info`
    - **Method Allowed**: `GET`
    - **Parameters**: None

    ### Response:
    The response is in JSON format with the following structure:
    ```bash
    {
    "email": "your-email@example.com",
    "current_datetime": "2025-01-30T09:30:00Z",
    "github_url": "https://github.com/yourusername/your-repo"
    }