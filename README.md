# Flask REST API

## Project Overview

This project demonstrates the development of a foundational REST API using Flask. The API handles JSON-based requests and performs validation, input parsing, and basic processing. It includes multiple endpoints such as health checks, simple "Hello World" responses, and a validation endpoint to verify the structure of JSON input.

This is part of a broader project to create a sign language interpreter backend.

---

## Endpoints

### **GET `/api/health`**  
Checks the health of the server.

- **Request**  
  - No parameters required.

- **Response**
  - **Success (200):**
    ```json
    {
        "status": "healthy"
    }
    ```

---

### **GET `/api/test`**  
Returns a simple "Hello, World!" message.

- **Request**  
  - No parameters required.

- **Response**
  - **Success (200):**
    ```json
    {
        "message": "Hello, World!"
    }
    ```

---

### **POST `/api/text`**  
Accepts a JSON input containing a `text` field and echoes the text back in the response, along with a confirmation message.

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
        "data": {
            "text": "Hello, Flask!"
        },
        "message": "Received your text!"
    }
    ```
  - **Error (400):**
    ```json
    {
        "error": "Missing 'text' in request body"
    }
    ```

---

### **POST `/api/validate`**  
Validates the structure of the provided JSON input and echoes the data back if it is valid.

- **Request**  
  - **Headers:** `Content-Type: application/json`  
  - **Body:**
    ```json
    {
        "name": "Alice",
        "age": 25
    }
    ```

- **Response**
  - **Success (200):**
    ```json
    {
        "data": {
            "name": "Alice",
            "age": 25
        },
        "message": "Valid data"
    }
    ```
  - **Error (400):**
    ```json
    {
        "error": "Invalid JSON format"
    }
    ```

---

## Setup and Installation

### Prerequisites
- Python 3.8 or higher.
- Virtual environment (recommended).

### Installation Steps
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

## Testing

### Using Hoppscotch
1. Open [Hoppscotch](https://hoppscotch.io/).
2. For each endpoint, configure the method (GET or POST), URL, headers, and body as described above.
3. Send the request and observe the response.

### Using Postman
1. Import the `postman/collection.json` into Postman.
2. Set up the environment to point to `http://127.0.0.1:5000`.
3. Run requests for each endpoint and validate responses.

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
├── postman/
│   └── collection.json  # Postman collection for testing
├── run.py               # Application entry point
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── .gitignore           # Ignored files
```

---

## Implementation Details

### Design Decisions
- Followed REST principles.
- Modularized routes and utility functions.
- Used Flask's built-in error handlers for better maintainability.

### Error Handling
- Handled 400 (Bad Request), 404 (Not Found), and 500 (Internal Server Error).
- Custom error messages for invalid inputs or missing data.

### Validation Rules
- Ensured `POST /api/text` requires a JSON payload with a `text` key.
- Validated all JSON inputs using Flask's request context.

---

## Automated Tests

### Running Tests
To run tests using `pytest`:
```bash
pytest tests/test_endpoints.py
```

### Test Cases
- Success scenarios for all endpoints.
- Validation of input formats and error scenarios.
- Response format and status code checks.

---

## License

This project is licensed under the MIT License.

---
