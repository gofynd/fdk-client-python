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

from .inventory.client import Inventory

from .configuration.client import Configuration

from .analytics.client import Analytics

from .discount.client import Discount

from .webhook.client import Webhook

from .audittrail.client import AuditTrail

from .logistic.client import Logistic


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
        
        self.inventory = Inventory(config)
        
        self.configuration = Configuration(config)
        
        self.analytics = Analytics(config)
        
        self.discount = Discount(config)
        
        self.webhook = Webhook(config)
        
        self.auditTrail = AuditTrail(config)
        
        self.logistic = Logistic(config)
        

    def application(self, applicationId):
        return PlatformApplicationClient(applicationId, self.config)

    def setExtraHeaders(self, header):
        if header and type(header) == dict:
            self.config.extraHeaders.append(header)
        else:
            raise FDKClientValidationError("Context value should be an dict")
