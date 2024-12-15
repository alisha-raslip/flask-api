# Flask REST API Project

## Overview

This Flask-based REST API project demonstrates foundational API development concepts, including JSON processing, input validation, and structured responses. It features multiple endpoints to process and validate data, as well as perform health checks. The API is designed for easy testing using tools like Hoppscotch or Postman.

---

## Endpoints

### 1. **POST `/api/text`**  
Processes a text input provided in the JSON body.

- **Request**
  - **Headers:** `Content-Type: application/json`
  - **Body:**
    ```json
    {
        "text": "Hello, Flask!"
    }
    ```

- **Response**
  - **Success (200):**
    ```json
    {
        "original_text": "Hello, Flask!",
        "processed_text": "HELLO, FLASK!"
    }
    ```
  - **Error (400):**
    ```json
    {
        "error": "Missing 'text' in request payload"
    }
    ```

---

### 2. **GET `/api/test`**  
Returns a basic "Hello World" message.

- **Request**
  - No parameters or headers required.

- **Response**
  - **Success (200):**
    ```json
    {
        "message": "Hello, World!"
    }
    ```

---

### 3. **POST `/api/validate`**  
Validates the structure of the provided JSON input.

- **Request**
  - **Headers:** `Content-Type: application/json`
  - **Body:**
    ```json
    {
        "key": "value"
    }
    ```

- **Response**
  - **Success (200):**
    ```json
    {
        "message": "JSON is valid"
    }
    ```
  - **Error (400):**
    ```json
    {
        "error": "Invalid JSON format"
    }
    ```

---

### 4. **GET `/api/health`**  
Performs a health check for the server.

- **Request**
  - No parameters or headers required.

- **Response**
  - **Success (200):**
    ```json
    {
        "status": "healthy"
    }
    ```

---

## Testing the API with Hoppscotch

### Setup Instructions
1. Open [Hoppscotch](https://hoppscotch.io/) in your browser.
2. For each endpoint, configure the method (GET or POST), URL, headers, and body as described below.

---

### **Testing `/api/text`**
1. Set the method to `POST`.
2. URL: `http://127.0.0.1:5000/api/text`
3. Add the header:
   - `Content-Type: application/json`
4. Add the body:
   ```json
   {
       "text": "Hello, Flask!"
   }
   ```
5. Click **Send** and check the response.

---

### **Testing `/api/test`**
1. Set the method to `GET`.
2. URL: `http://127.0.0.1:5000/api/test`
3. Click **Send** and check the response.

---

### **Testing `/api/validate`**
1. Set the method to `POST`.
2. URL: `http://127.0.0.1:5000/api/validate`
3. Add the header:
   - `Content-Type: application/json`
4. Add the body:
   ```json
   {
       "key": "value"
   }
   ```
5. Click **Send** and check the response.

---

### **Testing `/api/health`**
1. Set the method to `GET`.
2. URL: `http://127.0.0.1:5000/api/health`
3. Click **Send** and check the response.

---

## Project Setup

### Prerequisites
- Python 3.8 or higher.
- Virtual environment (optional but recommended).

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flask-api.git
   cd flask-api
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask server:
   ```bash
   flask run
   ```

---

## Folder Structure

```
flask-api/
├── app/
│   ├── __init__.py      # Flask app factory
│   ├── routes.py        # API endpoints
│   └── utils.py         # Utility functions
├── tests/
│   └── test_endpoints.py # Automated tests
├── run.py               # Application entry point
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── .gitignore           # Ignored files
```

---

## Automated Testing

### Run Tests
To run automated tests:
```bash
pytest tests/test_endpoints.py
```

---

## Contributing

1. Fork the repository.
2. Create a new branch (`feature-branch-name`).
3. Commit changes and push to the branch.
4. Open a Pull Request.

---

## License

This project is licensed under the MIT License.

---
