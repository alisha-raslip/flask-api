# Flask REST API

## Project Overview

This project implements a REST API using Flask to handle and process text data. It includes endpoints to perform operations such as processing text input (e.g., converting text to uppercase). The application demonstrates foundational API concepts such as request handling, input validation, JSON processing, and structured responses.

---

## Endpoints

### 1. **POST `/api/text`**
Processes the provided text input.

#### **Request**
- **Headers:**
  - `Content-Type: application/json`
- **Body:**
  ```json
  {
      "text": "Hello, Flask!"
  }
  ```

#### **Response**
- **Status Code:** `200 OK`
- **Body:**
  ```json
  {
      "original_text": "Hello, Flask!",
      "processed_text": "HELLO, FLASK!"
  }
  ```

#### **Error Responses**
- **Invalid Content Type:**
  ```json
  {
      "error": "Invalid content type. JSON required"
  }
  ```
- **Missing or Empty `text`:**
  ```json
  {
      "error": "'text' must be a non-empty string"
  }
  ```

---

## Setup and Installation

### **Prerequisites**
1. Python 3.8 or higher installed.
2. A virtual environment (optional but recommended).

### **Installation Steps**
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

4. Run the server:
   ```bash
   flask run
   ```

### **Testing the Server**
1. Use Postman, Hoppscotch, or `curl` to test the API.
2. Example request:
   ```bash
   curl -X POST http://127.0.0.1:5000/api/text -H "Content-Type: application/json" -d '{"text": "Hello"}'
   ```

---

## Project Structure

```
flask-api/
├── app/
│   ├── __init__.py      # Flask app factory
│   ├── routes.py        # API endpoints
│   └── utils.py         # Utility functions (if any)
├── tests/
│   └── test_endpoints.py # Automated tests
├── run.py               # Application entry point
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── .gitignore           # Ignored files
```

---

## Testing the API

### **Using Postman or Hoppscotch**
1. Set the method to `POST`.
2. URL: `http://127.0.0.1:5000/api/text`
3. Add the `Content-Type: application/json` header.
4. Provide the JSON body:
   ```json
   {
       "text": "Sample text"
   }
   ```

### **Using Curl**
```bash
curl -X POST http://127.0.0.1:5000/api/text -H "Content-Type: application/json" -d '{"text": "Sample text"}'
```

---

## Implementation Details

1. **Input Validation:** Ensures valid JSON and presence of `text` in the request body.
2. **Error Handling:** Responds with meaningful error messages for invalid requests.
3. **Response Formatting:** Provides consistent JSON responses with appropriate status codes.

---

## Future Enhancements

- Add more endpoints for text manipulation (e.g., reversing, translating).
- Integrate third-party APIs for advanced text processing.
- Implement database storage for text logs.

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

