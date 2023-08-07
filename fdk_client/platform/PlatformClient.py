"""Platform Client."""

from .PlatformApplicationClient import PlatformApplicationClient
from ..common.exceptions import FDKClientValidationError


from .audittrail.client import AuditTrail

from .billing.client import Billing

from .catalog.client import Catalog

from .common.client import Common

from .communication.client import Communication

from .companyprofile.client import CompanyProfile

from .configuration.client import Configuration

from .discount.client import Discount

from .filestorage.client import FileStorage

from .finance.client import Finance

from .inventory.client import Inventory

from .lead.client import Lead

from .order.client import Order

from .partner.client import Partner

from .payment.client import Payment

from .serviceability.client import Serviceability

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
        
        self.discount = Discount(config)
        
        self.fileStorage = FileStorage(config)
        
        self.finance = Finance(config)
        
        self.inventory = Inventory(config)
        
        self.lead = Lead(config)
        
        self.order = Order(config)
        
        self.partner = Partner(config)
        
        self.payment = Payment(config)
        
        self.serviceability = Serviceability(config)
        
        self.theme = Theme(config)
        
        self.webhook = Webhook(config)
        

    def application(self, applicationId):
        return PlatformApplicationClient(applicationId, self.config)

    def setExtraHeaders(self, header):
        if header and type(header) == dict:
            self.config.extraHeaders.append(header)
        else:
            raise FDKClientValidationError("Context value should be an dict")
