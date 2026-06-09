"""
File Manager - Handle file system operations
"""

import os
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class FileManager:
    """Manage file system operations"""
    
    def __init__(self):
        pass
    
    def list_directory(self, path: str = '.') -> list:
        """
        List files and directories
        
        Args:
            path: Directory path
            
        Returns:
            List of files and directories
        """
        try:
            expanded_path = os.path.expanduser(path)
            items = []
            
            if not os.path.exists(expanded_path):
                raise FileNotFoundError(f"Path not found: {path}")
            
            for item in os.listdir(expanded_path):
                item_path = os.path.join(expanded_path, item)
                is_dir = os.path.isdir(item_path)
                items.append({
                    'name': item,
                    'path': item_path,
                    'is_directory': is_dir,
                    'size': os.path.getsize(item_path) if os.path.isfile(item_path) else None
                })
            
            return sorted(items, key=lambda x: (not x['is_directory'], x['name']))
        except Exception as e:
            logger.error(f"Error listing directory {path}: {e}")
            raise
    
    def read_file(self, path: str) -> str:
        """
        Read file contents
        
        Args:
            path: File path
            
        Returns:
            File contents
        """
        try:
            expanded_path = os.path.expanduser(path)
            
            if not os.path.exists(expanded_path):
                raise FileNotFoundError(f"File not found: {path}")
            
            if not os.path.isfile(expanded_path):
                raise ValueError(f"Path is not a file: {path}")
            
            with open(expanded_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            logger.error(f"Error reading file {path}: {e}")
            raise
    
    def write_file(self, path: str, content: str) -> bool:
        """
        Write content to file
        
        Args:
            path: File path
            content: File content
            
        Returns:
            Success status
        """
        try:
            expanded_path = os.path.expanduser(path)
            
            # Create directories if they don't exist
            os.makedirs(os.path.dirname(expanded_path), exist_ok=True)
            
            with open(expanded_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        except Exception as e:
            logger.error(f"Error writing file {path}: {e}")
            raise
