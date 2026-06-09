"""
Offline AI - Local LLM integration using Ollama
"""

import os
import requests
import logging

logger = logging.getLogger(__name__)


class OfflineAI:
    """Handle offline AI interactions using local LLMs"""
    
    def __init__(self):
        self.ollama_host = os.getenv('OLLAMA_HOST', 'http://localhost:11434')
        self.model = os.getenv('OLLAMA_MODEL', 'llama2')
    
    def chat(self, message: str) -> str:
        """
        Send message to local LLM via Ollama
        
        Args:
            message: User message
            
        Returns:
            AI response
        """
        try:
            return self._chat_with_ollama(message)
        except Exception as e:
            logger.error(f"Offline AI error: {e}")
            raise
    
    def _chat_with_ollama(self, message: str) -> str:
        """Chat with Ollama local model"""
        try:
            url = f"{self.ollama_host}/api/generate"
            
            payload = {
                "model": self.model,
                "prompt": message,
                "stream": False,
                "temperature": 0.7
            }
            
            response = requests.post(url, json=payload, timeout=30)
            response.raise_for_status()
            
            result = response.json()
            return result.get('response', 'No response generated')
        except requests.exceptions.ConnectionError:
            logger.error(f"Cannot connect to Ollama at {self.ollama_host}")
            raise
        except Exception as e:
            logger.error(f"Ollama error: {e}")
            raise
    
    def check_connection(self) -> bool:
        """Check if Ollama is available"""
        try:
            response = requests.get(f"{self.ollama_host}/api/tags", timeout=5)
            return response.status_code == 200
        except:
            return False
