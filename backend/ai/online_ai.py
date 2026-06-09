"""
Online AI - Cloud-based AI integration (OpenAI, Claude)
"""

import os
import logging

logger = logging.getLogger(__name__)


class OnlineAI:
    """Handle online AI interactions using cloud APIs"""
    
    def __init__(self):
        self.openai_key = os.getenv('OPENAI_API_KEY')
        self.claude_key = os.getenv('CLAUDE_API_KEY')
        self.model = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')
    
    def chat(self, message: str) -> str:
        """
        Send message to online AI and get response
        
        Args:
            message: User message
            
        Returns:
            AI response
        """
        try:
            if self.openai_key:
                return self._chat_with_openai(message)
            elif self.claude_key:
                return self._chat_with_claude(message)
            else:
                return "Error: No API key configured for online mode"
        except Exception as e:
            logger.error(f"Online AI error: {e}")
            raise
    
    def _chat_with_openai(self, message: str) -> str:
        """Chat with OpenAI API"""
        try:
            import openai
            openai.api_key = self.openai_key
            
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are Cerebro, a helpful desktop AI assistant."},
                    {"role": "user", "content": message}
                ],
                temperature=0.7,
                max_tokens=500
            )
            
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"OpenAI API error: {e}")
            raise
    
    def _chat_with_claude(self, message: str) -> str:
        """Chat with Claude API"""
        try:
            import anthropic
            client = anthropic.Anthropic(api_key=self.claude_key)
            
            response = client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=500,
                system="You are Cerebro, a helpful desktop AI assistant.",
                messages=[
                    {"role": "user", "content": message}
                ]
            )
            
            return response.content[0].text
        except Exception as e:
            logger.error(f"Claude API error: {e}")
            raise
