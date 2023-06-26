"""Platform Client."""

from .PlatformApplicationClient import PlatformApplicationClient
from ..common.exceptions import FDKClientValidationError


from .common.client import Common

from .lead.client import Lead

from .billing.client import Billing

from .communication.client import Communication

from .payment.client import Payment

from .order.client import Order

from .catalog.client import Catalog

from .companyprofile.client import CompanyProfile

from .filestorage.client import FileStorage

from .configuration.client import Configuration

from .discount.client import Discount

from .partner.client import Partner

from .webhook.client import Webhook

from .audittrail.client import AuditTrail


class PlatformClient:
    def __init__(self, config):
        self.config = config
        
        self.common = Common(config)
        
        self.lead = Lead(config)
        
        self.billing = Billing(config)
        
        self.communication = Communication(config)
        
        self.payment = Payment(config)
        
        self.order = Order(config)
        
        self.catalog = Catalog(config)
        
        self.companyProfile = CompanyProfile(config)
        
        self.fileStorage = FileStorage(config)
        
        self.configuration = Configuration(config)
        
        self.discount = Discount(config)
        
        self.partner = Partner(config)
        
        self.webhook = Webhook(config)
        
        self.auditTrail = AuditTrail(config)
        

    def application(self, applicationId):
        return PlatformApplicationClient(applicationId, self.config)

    def setExtraHeaders(self, header):
        if header and type(header) == dict:
            self.config.extraHeaders.append(header)
        else:
            raise FDKClientValidationError("Context value should be an dict")
