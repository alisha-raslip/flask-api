from flask import Blueprint, request, jsonify
from marshmallow import Schema, fields, ValidationError

# Blueprint Setup
api_routes = Blueprint('api', __name__)

# Marshmallow Schema
class DataSchema(Schema):
    name = fields.Str(required=True)
    age = fields.Int(required=True)

schema = DataSchema()

# Health Check Endpoint
@api_routes.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

# Hello World Endpoint
@api_routes.route('/api/test', methods=['GET'])
def hello_world():
    return jsonify({"message": "Hello, World!"}), 200

# Text Processing Endpoint
@api_routes.route('/api/text', methods=['POST'])
def process_text():
    try:
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({"error": "Missing 'text' in request body"}), 400
        return jsonify({"message": "Received your text!", "data": data}), 200
    except Exception as e:
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

@api_routes.route('/api/validate', methods=['POST'])
def validate_data():
    try:
        data = request.get_json()
        validated_data = schema.load(data)
        return jsonify({"message": "Valid data", "data": validated_data}), 200
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

# Content Type Handling
@api_routes.route('/api/content', methods=['POST'])
def handle_content():
    try:
        content_type = request.content_type
        if content_type == 'application/json':
            data = request.get_json()
            return jsonify({"message": "JSON received", "data": data}), 200
        elif content_type == 'application/x-www-form-urlencoded':
            data = request.form.to_dict()
            return jsonify({"message": "Form data received", "data": data}), 200
        else:
            return jsonify({"error": f"Unsupported content type: {content_type}"}), 415
    except Exception as e:
        return jsonify({"error": "An error occurred", "details": str(e)}), 500