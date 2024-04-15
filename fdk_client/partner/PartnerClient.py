"""Partner Client."""

from ..common.exceptions import FDKClientValidationError


from .filestorage.client import FileStorage

from .lead.client import Lead

from .logistics.client import Logistics

from .theme.client import Theme

from .webhook.client import Webhook


class PartnerClient:
    def __init__(self, config):
        self.config = config
        
        self.fileStorage = FileStorage(config)
        
        self.lead = Lead(config)
        
        self.logistics = Logistics(config)
        
        self.theme = Theme(config)
        
        self.webhook = Webhook(config)
        

    def setExtraHeaders(self, header):
        if header and type(header) == dict:
            self.config.extraHeaders.append(header)
        else:
            raise FDKClientValidationError("Header value should be an dict")