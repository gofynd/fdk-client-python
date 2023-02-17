"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .bulkListingData import bulkListingData





from .BulkListingPage import BulkListingPage



class BulkListingResponse(BaseSchema):
    #  swagger.json

    
    error = fields.Str(required=False)
    
    data = fields.List(fields.Nested(bulkListingData, required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    page = fields.Nested(BulkListingPage, required=False)
    
