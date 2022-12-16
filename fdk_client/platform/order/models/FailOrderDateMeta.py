"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class FailOrderDateMeta(BaseSchema):
    #  swagger.json

    
    added_on_store = fields.Str(required=False)
    
    inventory_updated_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    