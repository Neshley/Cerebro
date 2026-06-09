"""
Cerebro Backend - Desktop AI Companion
Main Flask application server
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Import route handlers
from routes import ai_routes, system_routes, config_routes

# Register blueprints
app.register_blueprint(ai_routes.ai_bp)
app.register_blueprint(system_routes.system_bp)
app.register_blueprint(config_routes.config_bp)


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Cerebro Backend',
        'version': '1.0.0'
    }), 200


@app.route('/api/status', methods=['GET'])
def status():
    """Get system and AI status"""
    return jsonify({
        'backend_online': True,
        'ai_mode': os.getenv('AI_MODE', 'offline'),
        'internet_connected': check_internet_connection()
    }), 200


def check_internet_connection():
    """Check if system has internet connection"""
    try:
        import socket
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    logger.error(f"Internal server error: {error}")
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    # Development server
    app.run(debug=True, host='127.0.0.1', port=5000)
