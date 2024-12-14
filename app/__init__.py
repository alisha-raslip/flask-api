from flask import Flask, jsonify
from app.routes import api_routes

def create_app():
    app = Flask(__name__)

    # Register Blueprints
    app.register_blueprint(api_routes)

    # Global Error Handlers
    @app.errorhandler(400)
    def bad_request_error(e):
        return jsonify({"error": "Bad Request"}), 400

    @app.errorhandler(404)
    def not_found_error(e):
        return jsonify({"error": "Resource Not Found"}), 404

    @app.errorhandler(500)
    def internal_error(e):
        return jsonify({"error": "Internal Server Error"}), 500

    return app

