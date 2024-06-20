"""Platform Client."""

from ..common.exceptions import FDKClientValidationError


from .analytics.applicationClient import Analytics

from .cart.applicationClient import Cart

from .catalog.applicationClient import Catalog

from .communication.applicationClient import Communication

from .configuration.applicationClient import Configuration

from .content.applicationClient import Content

from .filestorage.applicationClient import FileStorage

from .lead.applicationClient import Lead

from .serviceability.applicationClient import Serviceability

from .order.applicationClient import Order

from .partner.applicationClient import Partner

from .payment.applicationClient import Payment

from .rewards.applicationClient import Rewards

from .share.applicationClient import Share

from .theme.applicationClient import Theme

from .user.applicationClient import User


class PlatformApplicationClient:
    def __init__(self, applicationId, config):
        self._conf = config
        
        self.analytics = Analytics(config, applicationId)
        
        self.cart = Cart(config, applicationId)
        
        self.catalog = Catalog(config, applicationId)
        
        self.communication = Communication(config, applicationId)
        
        self.configuration = Configuration(config, applicationId)
        
        self.content = Content(config, applicationId)
        
        self.fileStorage = FileStorage(config, applicationId)
        
        self.lead = Lead(config, applicationId)
        
        self.serviceability = Serviceability(config, applicationId)
        
        self.order = Order(config, applicationId)
        
        self.partner = Partner(config, applicationId)
        
        self.payment = Payment(config, applicationId)
        
        self.rewards = Rewards(config, applicationId)
        
        self.share = Share(config, applicationId)
        
        self.theme = Theme(config, applicationId)
        
        self.user = User(config, applicationId)
        

    async def setExtraHeaders(self, header):
        if header and type(header) == dict:
            self.config.extraHeaders.append(header)
        else:
            raise FDKClientValidationError("Context value should be an dict")
