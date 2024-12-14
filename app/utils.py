from flask import jsonify

def create_response(message, data=None, status_code=200):
    """
    Utility function to create a standardized JSON response.
    :param message: A string message describing the response.
    :param data: Additional data to include in the response (default is None).
    :param status_code: HTTP status code (default is 200).
    :return: A Flask JSON response.
    """
    response = {
        "message": message,
        "data": data if data is not None else {}
    }
    return jsonify(response), status_code


def validate_required_fields(data, required_fields):
    """
    Utility function to validate that all required fields are present in the request data.
    :param data: Dictionary containing the request data.
    :param required_fields: List of required field names.
    :return: Tuple (is_valid, errors)
             - is_valid: Boolean indicating if validation passed.
             - errors: List of missing fields or an empty list if no errors.
    """
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return False, {"missing_fields": missing_fields}
    return True, None


def log_error(error_message):
    """
    Utility function to log errors.
    This can be extended to integrate with logging frameworks like Python's logging module.
    :param error_message: The error message to log.
    """
    print(f"[ERROR] {error_message}")
