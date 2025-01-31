# HNG12 Backend Stage 0 Task

## Overview
This project implements a simple backend API using Python and Flask to return basic user information in JSON format. The API provides the following:
- Your registered email address.
- The current UTC datetime in ISO 8601 format.
- The URL to the GitHub repository for this project.

## Technology Stack
- **Programming Language**: Python 3.x
- **Framework**: Flask
- **CORS Handling**: Flask-CORS
- **Deployment**: The API is deployed on [Heroku](https://www.heroku.com/) (or your chosen platform)
  
## Features
- A public API that returns basic information in JSON format.
- Dynamic generation of the current date and time in ISO 8601 format (UTC).
- Proper handling of CORS requests.

## Setup Instructions

### Prerequisites
- Python 3.x
- `pip` (Python package installer)

### Steps to Run the Project Locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/HNG12-Backend.git
   cd HNG12-Backend
2. Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # for macOS/Linux
    source venv/Scripts/activate  # for Windows
3. Install dependencies:

    ```bash
    pip install -r requirements.txt
4. Run the application:

    ```bash
    python app.py
5. Access the API: Open your browser or API client (like Postman) and navigate to:

    ```bash
    http://127.0.0.1:5000/