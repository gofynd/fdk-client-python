"""Public Client."""

from .PublicConfig import PublicConfig
from ..common.exceptions import FDKClientValidationError


from .catalog.client import Catalog

from .configuration.client import Configuration

from .content.client import Content

from .partner.client import Partner

from .webhook.client import Webhook


class PublicClient:
    def __init__(self, config):
        if isinstance(config, PublicConfig):
            self.config = config
        else:
            self.config = PublicConfig(config)
        
        self.catalog = Catalog(self.config)
        
        self.configuration = Configuration(self.config)
        
        self.content = Content(self.config)
        
        self.partner = Partner(self.config)
        
        self.webhook = Webhook(self.config)
        
    
    def setExtraHeaders(self, header):
        if header and type(header) == dict:
            self.config.extraHeaders.append(header)
        else:
            raise FDKClientValidationError("Context value should be an dict")
