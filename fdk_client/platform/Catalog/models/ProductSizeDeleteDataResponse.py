"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class ProductSizeDeleteDataResponse(BaseSchema):
    #  swagger.json

    
    size = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
