# Flask REST API

## Project Overview

This project demonstrates the development of a foundational REST API using Flask. The API handles JSON-based requests and performs validation, input parsing, and basic processing. It includes multiple endpoints such as health checks, simple "Hello World" responses, a validation endpoint to verify the structure of JSON input, and a versatile content-type handler endpoint.

This is part of a broader project to create a sign language interpreter backend.

---

## Endpoints

### 1. **GET /api/health**
Checks the health of the server.

**Request**  
No parameters required.  

**Response**  
**Success (200):**
```json
{
    "status": "healthy"
}
```

---

### 2. **GET /api/test**  
Returns a simple "Hello, World!" message.  

**Request**  
No parameters required.  

**Response**  
**Success (200):**
```json
{
    "message": "Hello, World!"
}
```

---

### 3. **POST /api/text**  
Accepts a JSON input containing a text field and echoes the text back in the response, along with a confirmation message.  

**Request**  
**Headers:**  
`Content-Type: application/json`  
**Body:**
```json
{
    "text": "Hello, Flask!"
}
```

**Response**  
**Success (200):**
```json
{
    "data": {
        "text": "Hello, Flask!"
    },
    "message": "Received your text!"
}
```

**Error (400):**
```json
{
    "error": "Missing 'text' in request body"
}
```

---

### 4. **POST /api/validate**  
Validates the structure of the provided JSON input and echoes the data back if it is valid.

**Request**  
**Headers:**  
`Content-Type: application/json`  
**Body:**
```json
{
    "name": "Alice",
    "age": 25
}
```

**Response**  
**Success (200):**
```json
{
    "data": {
        "name": "Alice",
        "age": 25
    },
    "message": "Valid data"
}
```

**Error (400):**
```json
{
    "error": "Invalid JSON format"
}
```

**Error (500):**
```json
{
    "error": "An error occurred",
    "details": "Detailed error message here"
}
```

---

### 5. **POST /api/content**  
Handles different content types in requests and processes them accordingly.

**Request**  
**Headers:**  
The `Content-Type` header should specify one of the following:  
- `application/json`
- `application/x-www-form-urlencoded`

**Examples:**  
1. **For JSON Content-Type:**  
**Headers:**
`Content-Type: application/json`  
**Body:**
```json
{
    "key": "value"
}
```
**Response (200):**
```json
{
    "message": "JSON received",
    "data": {
        "key": "value"
    }
}
```

2. **For Form Data Content-Type:**  
**Headers:**
`Content-Type: application/x-www-form-urlencoded`  
**Body:**
```
key=value
```
**Response (200):**
```json
{
    "message": "Form data received",
    "data": {
        "key": "value"
    }
}
```

3. **Unsupported Content-Type:**  
**Response (415):**
```json
{
    "error": "Unsupported content type: text/plain"
}
```

**Error (500):**
```json
{
    "error": "An error occurred",
    "details": "Detailed error message here"
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

### Using Hoppscotch or Postman
- Configure each endpoint with the method (GET or POST), URL, headers, and body as described above.
- Send requests and observe responses.

### Automated Testing
Run tests using `pytest`:
```bash
pytest tests/test_endpoints.py
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
- 400 (Bad Request), 404 (Not Found), and 500 (Internal Server Error) handled gracefully.
- Custom error messages for invalid inputs or missing data.

### Validation Rules
- Ensured all JSON payloads are validated before processing.
- Supported multiple content types in `/api/content`.

---

## License

This project is licensed under the MIT License.  

--- 

