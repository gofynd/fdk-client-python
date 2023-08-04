"""Python code/fdk_client/internal/InternalConfig.py."""

from typing import Dict

class InternalConfig:
    def __init__(self, _conf: Dict):
        """Internal Config constructor."""
        self.domain = _conf.get("domain", "https://api.fynd.com")        
        self.extraHeaders = []
