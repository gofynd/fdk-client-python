"""Application Client."""

from ..common.exceptions import FDKClientValidationError
from .ApplicationValidator import LocationValidator


from .catalog.client import Catalog

from .cart.client import Cart

from .common.client import Common

from .lead.client import Lead

from .theme.client import Theme

from .user.client import User

from .content.client import Content

from .communication.client import Communication

from .share.client import Share

from .filestorage.client import FileStorage

from .configuration.client import Configuration

from .payment.client import Payment

from .rewards.client import Rewards

from .poscart.client import PosCart

from .logistic.client import Logistic


class ApplicationClient:
    def __init__(self, config):
        self.config = config
        self.catalog = Catalog(config)
        self.cart = Cart(config)
        self.common = Common(config)
        self.lead = Lead(config)
        self.theme = Theme(config)
        self.user = User(config)
        self.content = Content(config)
        self.communication = Communication(config)
        self.share = Share(config)
        self.fileStorage = FileStorage(config)
        self.configuration = Configuration(config)
        self.payment = Payment(config)
        self.rewards = Rewards(config)
        self.posCart = PosCart(config)
        self.logistic = Logistic(config)
        

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
