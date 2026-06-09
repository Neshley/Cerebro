"""
AI Routes - Handle AI interactions (online/offline)
"""

from flask import Blueprint, request, jsonify
import os
from ai.online_ai import OnlineAI
from ai.offline_ai import OfflineAI

ai_bp = Blueprint('ai', __name__, url_prefix='/api/ai')

# Initialize AI instances
online_ai = OnlineAI()
offline_ai = OfflineAI()


def get_ai_instance():
    """Get appropriate AI instance based on mode and connection"""
    mode = os.getenv('AI_MODE', 'offline')
    
    # Check internet connection
    try:
        import socket
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        internet_available = True
    except OSError:
        internet_available = False
    
    # Use online if mode is online and internet available
    if mode == 'online' and internet_available:
        return online_ai, 'online'
    else:
        return offline_ai, 'offline'


@ai_bp.route('/chat', methods=['POST'])
def chat():
    """Send message to AI and get response"""
    data = request.get_json()
    
    if not data or 'message' not in data:
        return jsonify({'error': 'Message required'}), 400
    
    message = data['message']
    
    try:
        ai_instance, mode = get_ai_instance()
        response = ai_instance.chat(message)
        
        return jsonify({
            'response': response,
            'mode': mode,
            'success': True
        }), 200
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500


@ai_bp.route('/mode', methods=['GET'])
def get_mode():
    """Get current AI mode"""
    ai_instance, mode = get_ai_instance()
    return jsonify({'mode': mode}), 200


@ai_bp.route('/models', methods=['GET'])
def get_models():
    """Get available models"""
    return jsonify({
        'online_models': ['gpt-4', 'gpt-3.5-turbo', 'claude-3'],
        'offline_models': ['llama2', 'mistral', 'neural-chat']
    }), 200
