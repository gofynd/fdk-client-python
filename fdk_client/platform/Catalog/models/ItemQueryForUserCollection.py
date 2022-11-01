"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class ItemQueryForUserCollection(BaseSchema):
    #  swagger.json

    
    item_id = fields.Int(required=False)
    
    action = fields.Str(required=False)
    
