"""Python code/fdk_client/admin/AdminConfig.py."""

from typing import Dict

class AdminConfig:
    def __init__(self, _conf: Dict):
        """Admin Config constructor."""
        self.domain = _conf.get("domain", "https://api.fynd.com")        
        self.extraHeaders = []
