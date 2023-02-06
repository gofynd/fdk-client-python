"""Public Client."""

from ..common.exceptions import FDKClientValidationError


from .configuration.client import Configuration

from .webhook.client import Webhook

from .inventory.client import Inventory


class PublicClient:
    def __init__(self, config):
        self.config = config
        
        self.configuration = Configuration(config)
        
        self.webhook = Webhook(config)
        
        self.inventory = Inventory(config)
        
    
    async def setExtraHeaders(self, header):
        if header and type(header) == dict:
            self.config.extraHeaders.append(header)
        else:
            raise FDKClientValidationError("Context value should be an dict")
