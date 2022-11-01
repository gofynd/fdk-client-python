"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class ProductBulkAssets(BaseSchema):
    #  swagger.json

    
    company_id = fields.Int(required=False)
    
    url = fields.Str(required=False)
    
    user = fields.Dict(required=False)
    
