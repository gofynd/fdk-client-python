"""Internal Client."""

from ..common.exceptions import FDKClientValidationError


from .filestorage.client import FileStorage


class InternalClient:
    def __init__(self, config):
        self.config = config
        
        self.fileStorage = FileStorage(config)
        
    
    def setExtraHeaders(self, header):
        if header and type(header) == dict:
            self.config.extraHeaders.append(header)
        else:
            raise FDKClientValidationError("Context value should be an dict")
