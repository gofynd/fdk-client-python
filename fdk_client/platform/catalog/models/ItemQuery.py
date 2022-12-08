"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class ItemQuery(BaseSchema):
    #  swagger.json

    
    brand_uid = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    
    item_code = fields.Str(required=False)
    
