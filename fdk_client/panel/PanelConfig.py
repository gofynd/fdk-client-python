"""Python code/fdk_client/panel/PanelConfig.py."""

from typing import Dict

class PanelConfig:
    def __init__(self, _conf: Dict):
        """Panel Config constructor."""
        self.domain = _conf.get("domain", "https://api.fynd.com")        
        self.extraHeaders = []
