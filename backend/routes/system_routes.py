"""
System Routes - Handle system access and commands
"""

from flask import Blueprint, request, jsonify
from system.file_manager import FileManager
from system.process_manager import ProcessManager
from system.web_access import WebAccess

system_bp = Blueprint('system', __name__, url_prefix='/api/system')

# Initialize system managers
file_manager = FileManager()
process_manager = ProcessManager()
web_access = WebAccess()


@system_bp.route('/files/list', methods=['POST'])
def list_files():
    """List files in a directory"""
    data = request.get_json()
    path = data.get('path', '.')
    
    try:
        files = file_manager.list_directory(path)
        return jsonify({
            'files': files,
            'path': path,
            'success': True
        }), 200
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500


@system_bp.route('/files/read', methods=['POST'])
def read_file():
    """Read file contents"""
    data = request.get_json()
    path = data.get('path')
    
    if not path:
        return jsonify({'error': 'Path required'}), 400
    
    try:
        content = file_manager.read_file(path)
        return jsonify({
            'content': content,
            'path': path,
            'success': True
        }), 200
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500


@system_bp.route('/processes/list', methods=['GET'])
def list_processes():
    """List running processes"""
    try:
        processes = process_manager.list_processes()
        return jsonify({
            'processes': processes,
            'success': True
        }), 200
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500


@system_bp.route('/web/open', methods=['POST'])
def open_website():
    """Open a website in default browser"""
    data = request.get_json()
    url = data.get('url')
    
    if not url:
        return jsonify({'error': 'URL required'}), 400
    
    try:
        web_access.open_url(url)
        return jsonify({
            'url': url,
            'success': True
        }), 200
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500
