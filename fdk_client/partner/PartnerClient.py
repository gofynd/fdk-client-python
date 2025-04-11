"""Partner Client."""

from ..common.exceptions import FDKClientValidationError
from ..common.custom_request import custom_request


from .authorization.client import Authorization

from .catalog.client import Catalog

from .filestorage.client import FileStorage

from .lead.client import Lead

from .logistics.client import Logistics

from .payment.client import Payment

from .theme.client import Theme

from .webhook.client import Webhook


class PartnerClient:
    def __init__(self, config):
        self.config = config
        
        self.authorization = Authorization(config)
        
        self.catalog = Catalog(config)
        
        self.fileStorage = FileStorage(config)
        
        self.lead = Lead(config)
        
        self.logistics = Logistics(config)
        
        self.payment = Payment(config)
        
        self.theme = Theme(config)
        
        self.webhook = Webhook(config)
        

    def setExtraHeaders(self, header):
        if header and type(header) == dict:
            self.config.extraHeaders.append(header)
        else:
            raise FDKClientValidationError("Header value should be an dict")

    async def request(self, method, url, query={}, body={}, headers={}):
        return await custom_request(self, method, url, query, body, headers)