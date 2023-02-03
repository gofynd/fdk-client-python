"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class ItemQuery(BaseSchema):
    #  swagger.json

    
    item_code = fields.Str(required=False)
    
    brand_uid = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    
