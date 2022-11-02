"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class ProductBulkAssets(BaseSchema):
    #  swagger.json

    
    url = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    user = fields.Dict(required=False)
    
