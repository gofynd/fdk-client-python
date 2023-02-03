"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class DateMeta(BaseSchema):
    #  swagger.json

    
    inventory_updated_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    added_on_store = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
