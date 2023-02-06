"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .BulkListingPage import BulkListingPage



from .bulkListingData import bulkListingData







class BulkListingResponse(BaseSchema):
    #  swagger.json

    
    page = fields.Nested(BulkListingPage, required=False)
    
    data = fields.List(fields.Nested(bulkListingData, required=False), required=False)
    
    error = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
