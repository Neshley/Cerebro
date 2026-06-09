"""
Todo Backend - Flask API for todo management with local storage
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime
from pathlib import Path

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure storage
DATA_DIR = Path('data')
DATA_DIR.mkdir(exist_ok=True)
TODOS_FILE = DATA_DIR / 'todos.json'


# ==================== Helper Functions ====================

def load_todos():
    """Load todos from JSON file"""
    if TODOS_FILE.exists():
        with open(TODOS_FILE, 'r') as f:
            return json.load(f)
    return []


def save_todos(todos):
    """Save todos to JSON file"""
    with open(TODOS_FILE, 'w') as f:
        json.dump(todos, f, indent=2)


def generate_id():
    """Generate unique todo ID"""
    todos = load_todos()
    if not todos:
        return 1
    return max(todo['id'] for todo in todos) + 1


# ==================== Health Check ====================

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Todo Backend',
        'version': '1.0.0'
    }), 200


# ==================== Todo CRUD Endpoints ====================

@app.route('/api/todos', methods=['GET'])
def get_todos():
    """Get all todos"""
    try:
        todos = load_todos()
        
        # Optional filtering
        status = request.args.get('status')  # active, completed, all
        category = request.args.get('category')
        
        if status == 'active':
            todos = [t for t in todos if not t.get('completed')]
        elif status == 'completed':
            todos = [t for t in todos if t.get('completed')]
        
        if category:
            todos = [t for t in todos if t.get('category') == category]
        
        return jsonify({
            'todos': todos,
            'total': len(todos),
            'success': True
        }), 200
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500


@app.route('/api/todos', methods=['POST'])
def create_todo():
    """Create a new todo"""
    try:
        data = request.get_json()
        
        if not data or 'title' not in data:
            return jsonify({'error': 'Title is required'}), 400
        
        todos = load_todos()
        
        new_todo = {
            'id': generate_id(),
            'title': data['title'],
            'description': data.get('description', ''),
            'category': data.get('category', 'General'),
            'priority': data.get('priority', 'medium'),  # low, medium, high
            'completed': False,
            'dueDate': data.get('dueDate', None),
            'createdAt': datetime.now().isoformat(),
            'updatedAt': datetime.now().isoformat()
        }
        
        todos.append(new_todo)
        save_todos(todos)
        
        return jsonify({
            'todo': new_todo,
            'success': True
        }), 201
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500


@app.route('/api/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    """Get a specific todo"""
    try:
        todos = load_todos()
        todo = next((t for t in todos if t['id'] == todo_id), None)
        
        if not todo:
            return jsonify({'error': 'Todo not found'}), 404
        
        return jsonify({
            'todo': todo,
            'success': True
        }), 200
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500


@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """Update a todo"""
    try:
        data = request.get_json()
        todos = load_todos()
        
        todo = next((t for t in todos if t['id'] == todo_id), None)
        if not todo:
            return jsonify({'error': 'Todo not found'}), 404
        
        # Update fields
        if 'title' in data:
            todo['title'] = data['title']
        if 'description' in data:
            todo['description'] = data['description']
        if 'category' in data:
            todo['category'] = data['category']
        if 'priority' in data:
            todo['priority'] = data['priority']
        if 'completed' in data:
            todo['completed'] = data['completed']
        if 'dueDate' in data:
            todo['dueDate'] = data['dueDate']
        
        todo['updatedAt'] = datetime.now().isoformat()
        
        save_todos(todos)
        
        return jsonify({
            'todo': todo,
            'success': True
        }), 200
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500


@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """Delete a todo"""
    try:
        todos = load_todos()
        todos = [t for t in todos if t['id'] != todo_id]
        save_todos(todos)
        
        return jsonify({
            'success': True,
            'message': 'Todo deleted'
        }), 200
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500


# ==================== Bulk Operations ====================

@app.route('/api/todos/bulk/delete', methods=['POST'])
def bulk_delete_todos():
    """Delete multiple todos"""
    try:
        data = request.get_json()
        ids = data.get('ids', [])
        
        todos = load_todos()
        todos = [t for t in todos if t['id'] not in ids]
        save_todos(todos)
        
        return jsonify({
            'success': True,
            'deleted': len(ids)
        }), 200
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500


@app.route('/api/todos/bulk/update', methods=['POST'])
def bulk_update_todos():
    """Update multiple todos"""
    try:
        data = request.get_json()
        ids = data.get('ids', [])
        updates = data.get('updates', {})
        
        todos = load_todos()
        for todo in todos:
            if todo['id'] in ids:
                for key, value in updates.items():
                    todo[key] = value
                todo['updatedAt'] = datetime.now().isoformat()
        
        save_todos(todos)
        
        return jsonify({
            'success': True,
            'updated': len(ids)
        }), 200
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500


# ==================== Statistics ====================

@app.route('/api/todos/stats', methods=['GET'])
def get_stats():
    """Get todo statistics"""
    try:
        todos = load_todos()
        
        stats = {
            'total': len(todos),
            'completed': sum(1 for t in todos if t.get('completed')),
            'active': sum(1 for t in todos if not t.get('completed')),
            'highPriority': sum(1 for t in todos if t.get('priority') == 'high'),
            'categories': {}
        }
        
        # Count by category
        for todo in todos:
            category = todo.get('category', 'General')
            stats['categories'][category] = stats['categories'].get(category, 0) + 1
        
        return jsonify({
            'stats': stats,
            'success': True
        }), 200
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500


# ==================== Categories ====================

@app.route('/api/categories', methods=['GET'])
def get_categories():
    """Get all categories"""
    try:
        todos = load_todos()
        categories = set(todo.get('category', 'General') for todo in todos)
        categories = sorted(list(categories))
        
        return jsonify({
            'categories': categories,
            'success': True
        }), 200
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500


# ==================== Export/Import ====================

@app.route('/api/todos/export', methods=['GET'])
def export_todos():
    """Export todos as JSON"""
    try:
        todos = load_todos()
        return jsonify({
            'todos': todos,
            'exportDate': datetime.now().isoformat(),
            'success': True
        }), 200
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500


@app.route('/api/todos/import', methods=['POST'])
def import_todos():
    """Import todos from JSON"""
    try:
        data = request.get_json()
        new_todos = data.get('todos', [])
        
        # Adjust IDs to avoid conflicts
        existing_todos = load_todos()
        max_id = max((t['id'] for t in existing_todos), default=0)
        
        for i, todo in enumerate(new_todos):
            todo['id'] = max_id + i + 1
        
        all_todos = existing_todos + new_todos
        save_todos(all_todos)
        
        return jsonify({
            'success': True,
            'imported': len(new_todos),
            'total': len(all_todos)
        }), 200
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500


# ==================== Error Handlers ====================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)
