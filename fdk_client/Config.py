"""Python code/fdk_client//Config.py."""

from typing import Dict

class Config:
    def __init__(self, _conf: Dict):
        """ Config constructor."""
        self.domain = _conf.get("domain", "https://api.fynd.com")        
        self.extraHeaders = []
