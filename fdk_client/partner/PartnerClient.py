"""Partner Client."""

from .PartnerConfig import PartnerConfig
from ..common.exceptions import FDKClientValidationError
from ..common.custom_request import custom_request


from .filestorage.client import FileStorage

from .lead.client import Lead

from .logistics.client import Logistics

from .theme.client import Theme

from .webhook.client import Webhook


class PartnerClient:
    def __init__(self, config):
        if isinstance(config, PartnerConfig):
            self.config = config
        else:
            self.config = PartnerConfig(config)
        
        self.fileStorage = FileStorage(self.config)
        
        self.lead = Lead(self.config)
        
        self.logistics = Logistics(self.config)
        
        self.theme = Theme(self.config)
        
        self.webhook = Webhook(self.config)
        

    def setExtraHeaders(self, header):
        if header and type(header) == dict:
            self.config.extraHeaders.append(header)
        else:
            raise FDKClientValidationError("Header value should be an dict")
            
    def getAccesstokenObj(self, grant_type="", refresh_token="", code=""):
        return self.config.oauthClient.getAccesstokenObj(grant_type, refresh_token, code)
    
    def setToken(self, token):
        self.config.oauthClient.setToken(token)

    async def request(self, method, url, query={}, body={}, headers={}):
        return await custom_request(self, method, url, query, body, headers)
