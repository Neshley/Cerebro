"""
Configuration Routes - Handle system configuration
"""

from flask import Blueprint, request, jsonify
import os

config_bp = Blueprint('config', __name__, url_prefix='/api/config')


@config_bp.route('/settings', methods=['GET'])
def get_settings():
    """Get current settings"""
    return jsonify({
        'ai_mode': os.getenv('AI_MODE', 'offline'),
        'backend_port': os.getenv('BACKEND_PORT', 5000),
        'ollama_host': os.getenv('OLLAMA_HOST', 'http://localhost:11434')
    }), 200


@config_bp.route('/settings/ai-mode', methods=['POST'])
def set_ai_mode():
    """Change AI mode"""
    data = request.get_json()
    mode = data.get('mode', 'offline')
    
    if mode not in ['online', 'offline']:
        return jsonify({'error': 'Mode must be online or offline'}), 400
    
    # In production, you'd save this to a config file
    os.environ['AI_MODE'] = mode
    
    return jsonify({
        'mode': mode,
        'success': True
    }), 200
