"""
Web Access - Handle web browsing and URL operations
"""

import webbrowser
import requests
import logging
from urllib.parse import urljoin, urlparse

logger = logging.getLogger(__name__)


class WebAccess:
    """Handle web operations"""
    
    def __init__(self):
        pass
    
    def open_url(self, url: str) -> bool:
        """
        Open URL in default browser
        
        Args:
            url: URL to open
            
        Returns:
            Success status
        """
        try:
            # Ensure URL has protocol
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url
            
            webbrowser.open(url)
            logger.info(f"Opened URL: {url}")
            return True
        except Exception as e:
            logger.error(f"Error opening URL {url}: {e}")
            raise
    
    def fetch_content(self, url: str) -> str:
        """
        Fetch content from URL
        
        Args:
            url: URL to fetch
            
        Returns:
            Page content
        """
        try:
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url
            
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            return response.text
        except Exception as e:
            logger.error(f"Error fetching URL {url}: {e}")
            raise
    
    def is_valid_url(self, url: str) -> bool:
        """
        Validate URL format
        
        Args:
            url: URL to validate
            
        Returns:
            Validity status
        """
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except:
            return False
