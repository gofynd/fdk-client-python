"""Panel Client."""

from ..common.exceptions import FDKClientValidationError



class PanelClient:
    def __init__(self, config):
        self.config = config
        
    
    def setExtraHeaders(self, header):
        if header and type(header) == dict:
            self.config.extraHeaders.append(header)
        else:
            raise FDKClientValidationError("Context value should be an dict")
