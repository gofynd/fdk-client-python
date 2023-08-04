"""Admin Client."""

from ..common.exceptions import FDKClientValidationError


from .catalog.client import Catalog

from .communication.client import Communication

from .finance.client import Finance

from .partner.client import Partner

from .payment.client import Payment


class AdminClient:
    def __init__(self, config):
        self.config = config
        
        self.catalog = Catalog(config)
        
        self.communication = Communication(config)
        
        self.finance = Finance(config)
        
        self.partner = Partner(config)
        
        self.payment = Payment(config)
        
    
    def setExtraHeaders(self, header):
        if header and type(header) == dict:
            self.config.extraHeaders.append(header)
        else:
            raise FDKClientValidationError("Context value should be an dict")
