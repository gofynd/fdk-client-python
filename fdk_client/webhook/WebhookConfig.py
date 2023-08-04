"""Python code/fdk_client/webhook/WebhookConfig.py."""

from typing import Dict

class WebhookConfig:
    def __init__(self, _conf: Dict):
        """Webhook Config constructor."""
        self.domain = _conf.get("domain", "https://api.fynd.com")        
        self.extraHeaders = []
