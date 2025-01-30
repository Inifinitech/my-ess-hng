# FastAPI Project: User Details API

This is a simple FastAPI project that provides an API to retrieve user details, including an email, a GitHub URL, and a timestamp in ISO 8601 format. The API is designed to handle Cross-Origin Resource Sharing (CORS) appropriately, making it suitable for use with frontend applications.

---

## Table of Contents
1. [Project Description](#project-description)
2. [Setup Instructions](#setup-instructions)
3. [API Documentation](#api-documentation)
   - [Endpoint URL](#endpoint-url)
   - [Request/Response Format](#requestresponse-format)
   - [Example Usage](#example-usage)

---

## Project Description

This project is a FastAPI-based API that serves user details. It includes the following features:
- A root endpoint (`/`) that returns a welcome message.
- A `/get-details` endpoint that returns user details, including:
  - Email address.
  - GitHub URL.
  - A timestamp in ISO 8601 format.
- Proper CORS configuration to allow requests from specified origins.

---

## Setup Instructions

Follow these steps to set up and run the project locally.

### Prerequisites
- Python 3.7 or higher.
- `pip` (Python package manager).

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

2. **Create a virtual environment** (optional)
    ```bash
    python -m venv venv
    source venv/bin/activate

3. **Install Dependencies**
    ```bash
    pip install "fastapi[all]" uvicorn orjson

4. Run the server
    ```bash
    uvicorn main:app --reload


### API Documentation

## Endpoint URL

 . Base URL: ```http://127.0.0.1:8000```

## Endpoint

1. Root Endpoint(```/```)
    . Method: ```GET```
    . Description: Returns a welcome message.

2. Get User Details(```/get-details```)
    . Method: ```GET```
    . Description: Returns user details, including email, GitHub URL, and a timestamp in ISO 8601


### Example Usage

Using ```curl``` to Test the API

 1. Access the root endpoint:
    ```curl -X GET http://127.0.0.1:8000/```

  **Response:**

     {
        "message": "Welcome"
     }

 2. Access the ```/get-details``` endpoint:
    ``` curl -X GET http://127.0.0.1:8000/get-details```

  **Response:**

    {
        "email": "kuriaisac@gmail.com",
        "local-time": "2023-10-05T14:30:45Z",
        "github-url": "https://github.com/Inifinitech/my-ess-hng"
    }

### CORS Configuration

The API is configured to allow requests from the following origins:

. ```http://localhost```

## Backlink
**https://hng.tech/hire/python-developers**

