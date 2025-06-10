"""Platform Client."""

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
        self.config = config
        
        self.auditTrail = AuditTrail(config)
        
        self.billing = Billing(config)
        
        self.catalog = Catalog(config)
        
        self.common = Common(config)
        
        self.communication = Communication(config)
        
        self.companyProfile = CompanyProfile(config)
        
        self.configuration = Configuration(config)
        
        self.content = Content(config)
        
        self.discount = Discount(config)
        
        self.fileStorage = FileStorage(config)
        
        self.lead = Lead(config)
        
        self.serviceability = Serviceability(config)
        
        self.order = Order(config)
        
        self.payment = Payment(config)
        
        self.theme = Theme(config)
        
        self.webhook = Webhook(config)
        

    def application(self, applicationId):
        return PlatformApplicationClient(applicationId, self.config)

    def setExtraHeaders(self, header):
        if header and type(header) == dict:
            self.config.extraHeaders.append(header)
        else:
            raise FDKClientValidationError("Context value should be an dict")

    async def request(self, method, url, query={}, body={}, headers={}):
        return await custom_request(self, method, url, query, body, headers)
