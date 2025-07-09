"""Platform Client."""

from .PlatformConfig import PlatformConfig
from .PlatformApplicationClient import PlatformApplicationClient
from ..common.exceptions import FDKClientValidationError
from ..common.custom_request import custom_request


from .audittrail.client import AuditTrail

from .billing.client import Billing

from .catalog.client import Catalog

from .common.client import Common

from .communication.client import Communication

from .companyprofile.client import CompanyProfile

from .configuration.client import Configuration

from .content.client import Content

from .discount.client import Discount

from .filestorage.client import FileStorage

from .lead.client import Lead

from .serviceability.client import Serviceability

from .order.client import Order

from .payment.client import Payment

from .theme.client import Theme

from .webhook.client import Webhook


class PlatformClient:
    def __init__(self, config):
        if isinstance(config, PlatformConfig):
            self.config = config
        else:
            self.config = PlatformConfig(config)
        
        self.auditTrail = AuditTrail(self.config)
        
        self.billing = Billing(self.config)
        
        self.catalog = Catalog(self.config)
        
        self.common = Common(self.config)
        
        self.communication = Communication(self.config)
        
        self.companyProfile = CompanyProfile(self.config)
        
        self.configuration = Configuration(self.config)
        
        self.content = Content(self.config)
        
        self.discount = Discount(self.config)
        
        self.fileStorage = FileStorage(self.config)
        
        self.lead = Lead(self.config)
        
        self.serviceability = Serviceability(self.config)
        
        self.order = Order(self.config)
        
        self.payment = Payment(self.config)
        
        self.theme = Theme(self.config)
        
        self.webhook = Webhook(self.config)
        

    def application(self, applicationId):
        return PlatformApplicationClient(applicationId, self.config)

    def setExtraHeaders(self, header):
        if header and type(header) == dict:
            self.config.extraHeaders.append(header)
        else:
            raise FDKClientValidationError("Context value should be an dict")
    
    def getAccesstokenObj(self, grant_type="", refresh_token="", code=""):
        return self.config.oauthClient.getAccesstokenObj(grant_type, refresh_token, code)
    
    def setToken(self, token):
        self.config.oauthClient.setToken(token)

    async def request(self, method, url, query={}, body={}, headers={}):
        return await custom_request(self, method, url, query, body, headers)
