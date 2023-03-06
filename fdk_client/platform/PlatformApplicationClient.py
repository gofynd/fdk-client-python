"""Platform Client."""

from ..common.exceptions import FDKClientValidationError


from .lead.applicationClient import Lead

from .feedback.applicationClient import Feedback

from .theme.applicationClient import Theme

from .user.applicationClient import User

from .content.applicationClient import Content

from .communication.applicationClient import Communication

from .payment.applicationClient import Payment

from .order.applicationClient import Order

from .catalog.applicationClient import Catalog

from .filestorage.applicationClient import FileStorage

from .share.applicationClient import Share

from .configuration.applicationClient import Configuration

from .cart.applicationClient import Cart

from .rewards.applicationClient import Rewards

from .analytics.applicationClient import Analytics

from .partner.applicationClient import Partner


class PlatformApplicationClient:
    def __init__(self, applicationId, config):
        
        self.lead = Lead(config, applicationId)
        
        self.feedback = Feedback(config, applicationId)
        
        self.theme = Theme(config, applicationId)
        
        self.user = User(config, applicationId)
        
        self.content = Content(config, applicationId)
        
        self.communication = Communication(config, applicationId)
        
        self.payment = Payment(config, applicationId)
        
        self.order = Order(config, applicationId)
        
        self.catalog = Catalog(config, applicationId)
        
        self.fileStorage = FileStorage(config, applicationId)
        
        self.share = Share(config, applicationId)
        
        self.configuration = Configuration(config, applicationId)
        
        self.cart = Cart(config, applicationId)
        
        self.rewards = Rewards(config, applicationId)
        
        self.analytics = Analytics(config, applicationId)
        
        self.partner = Partner(config, applicationId)
        

    async def setExtraHeaders(self, header):
        if header and type(header) == dict:
            self.config.extraHeaders.append(header)
        else:
            raise FDKClientValidationError("Context value should be an dict")
