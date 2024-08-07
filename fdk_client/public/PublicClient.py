"""Public Client."""

from ..common.exceptions import FDKClientValidationError


from .billing.client import Billing

from .configuration.client import Configuration

from .content.client import Content

from .partner.client import Partner

from .webhook.client import Webhook


class PublicClient:
    def __init__(self, config):
        self.config = config
        
        self.billing = Billing(config)
        
        self.configuration = Configuration(config)
        
        self.content = Content(config)
        
        self.partner = Partner(config)
        
        self.webhook = Webhook(config)
        
    
    def setExtraHeaders(self, header):
        if header and type(header) == dict:
            self.config.extraHeaders.append(header)
        else:
            raise FDKClientValidationError("Context value should be an dict")
