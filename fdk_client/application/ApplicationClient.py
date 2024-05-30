"""Application Client."""

from ..common.exceptions import FDKClientValidationError
from .ApplicationValidator import LocationValidator


from .cart.client import Cart

from .catalog.client import Catalog

from .common.client import Common

from .communication.client import Communication

from .configuration.client import Configuration

from .content.client import Content

from .filestorage.client import FileStorage

from .lead.client import Lead

from .logistic.client import Logistic

from .order.client import Order

from .payment.client import Payment

from .rewards.client import Rewards

from .share.client import Share

from .theme.client import Theme

from .user.client import User


class ApplicationClient:
    def __init__(self, config):
        self.config = config
        self.cart = Cart(config)
        self.catalog = Catalog(config)
        self.common = Common(config)
        self.communication = Communication(config)
        self.configuration = Configuration(config)
        self.content = Content(config)
        self.fileStorage = FileStorage(config)
        self.lead = Lead(config)
        self.logistic = Logistic(config)
        self.order = Order(config)
        self.payment = Payment(config)
        self.rewards = Rewards(config)
        self.share = Share(config)
        self.theme = Theme(config)
        self.user = User(config)
        

    def setCookie(self, cookie):
        self.config.cookies = cookie

    def setLocationDetails(self, locationDetails):
        schema = LocationValidator.validateLocationObj()
        schema.dump(schema.load(locationDetails))
        self.config.locationDetails = locationDetails

    def setExtraHeaders(self, header):
        if header and type(header) == dict:
            self.config.extraHeaders.append(header)
        else:
            raise FDKClientValidationError("Context value should be an dict")
