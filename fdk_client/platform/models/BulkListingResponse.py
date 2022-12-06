"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .bulkListingData import bulkListingData





from .BulkListingPage import BulkListingPage


class BulkListingResponse(BaseSchema):
    # Order swagger.json

    
    data = fields.List(fields.Nested(bulkListingData, required=False), required=False)
    
    error = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    page = fields.Nested(BulkListingPage, required=False)
    

