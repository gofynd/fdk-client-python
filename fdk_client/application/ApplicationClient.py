"""Application Client."""

from .ApplicationConfig import ApplicationConfig
from ..common.exceptions import FDKClientValidationError
from .ApplicationValidator import LocationValidator
from ..common.custom_request import custom_request


from .cart.client import Cart

from .catalog.client import Catalog

from .common.client import Common

from .communication.client import Communication

from .configuration.client import Configuration

from .content.client import Content

from .filestorage.client import FileStorage

from .finance.client import Finance

from .lead.client import Lead

from .logistic.client import Logistic

from .order.client import Order

from .payment.client import Payment

from .share.client import Share

from .theme.client import Theme

from .user.client import User

from .webhook.client import Webhook


class ApplicationClient:
    def __init__(self, config):
        if isinstance(config, ApplicationConfig):
            self.config = config
        else:
            self.config = ApplicationConfig(config)
        self.cart = Cart(self.config)
        self.catalog = Catalog(self.config)
        self.common = Common(self.config)
        self.communication = Communication(self.config)
        self.configuration = Configuration(self.config)
        self.content = Content(self.config)
        self.fileStorage = FileStorage(self.config)
        self.finance = Finance(self.config)
        self.lead = Lead(self.config)
        self.logistic = Logistic(self.config)
        self.order = Order(self.config)
        self.payment = Payment(self.config)
        self.share = Share(self.config)
        self.theme = Theme(self.config)
        self.user = User(self.config)
        self.webhook = Webhook(self.config)
        

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

    async def request(self, method, url, query={}, body={}, headers={}):
        return await custom_request(self, method, url, query, body, headers, "application")
