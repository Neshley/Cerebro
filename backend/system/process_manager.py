"""
Process Manager - Handle system processes
"""

import psutil
import logging

logger = logging.getLogger(__name__)


class ProcessManager:
    """Manage system processes"""
    
    def __init__(self):
        pass
    
    def list_processes(self) -> list:
        """
        List running processes
        
        Returns:
            List of process information
        """
        try:
            processes = []
            
            for proc in psutil.process_iter(['pid', 'name', 'status']):
                try:
                    processes.append({
                        'pid': proc.info['pid'],
                        'name': proc.info['name'],
                        'status': proc.info['status']
                    })
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
            
            return processes
        except Exception as e:
            logger.error(f"Error listing processes: {e}")
            raise
    
    def kill_process(self, pid: int) -> bool:
        """
        Kill a process
        
        Args:
            pid: Process ID
            
        Returns:
            Success status
        """
        try:
            proc = psutil.Process(pid)
            proc.terminate()
            return True
        except Exception as e:
            logger.error(f"Error killing process {pid}: {e}")
            raise
    
    def get_process_info(self, pid: int) -> dict:
        """
        Get detailed process information
        
        Args:
            pid: Process ID
            
        Returns:
            Process information
        """
        try:
            proc = psutil.Process(pid)
            return {
                'pid': proc.pid,
                'name': proc.name(),
                'status': proc.status(),
                'memory_percent': proc.memory_percent(),
                'cpu_percent': proc.cpu_percent(interval=1)
            }
        except Exception as e:
            logger.error(f"Error getting process info for {pid}: {e}")
            raise
