"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class ProductSizeDeleteDataResponse(BaseSchema):
    #  swagger.json

    
    item_id = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
