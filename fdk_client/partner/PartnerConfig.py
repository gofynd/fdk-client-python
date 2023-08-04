"""Python code/fdk_client/partner/PartnerConfig.py."""

from typing import Dict

class PartnerConfig:
    def __init__(self, _conf: Dict):
        """Partner Config constructor."""
        self.domain = _conf.get("domain", "https://api.fynd.com")        
        self.extraHeaders = []
