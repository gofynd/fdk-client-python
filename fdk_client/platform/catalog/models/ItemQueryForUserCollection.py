"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class ItemQueryForUserCollection(BaseSchema):
    #  swagger.json

    
    action = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
