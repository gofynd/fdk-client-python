"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .BulkListingPage import BulkListingPage





from .bulkListingData import bulkListingData


class BulkListingResponse(BaseSchema):
    # Order swagger.json

    
    page = fields.Nested(BulkListingPage, required=False)
    
    success = fields.Boolean(required=False)
    
    error = fields.Str(required=False)
    
    data = fields.List(fields.Nested(bulkListingData, required=False), required=False)
    

