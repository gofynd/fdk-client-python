"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .BulkListingPage import BulkListingPage

from .bulkListingData import bulkListingData


class BulkListingResponse(BaseSchema):
    # Orders swagger.json

    
    error = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    page = fields.Nested(BulkListingPage, required=False)
    
    data = fields.List(fields.Nested(bulkListingData, required=False), required=False)
    

