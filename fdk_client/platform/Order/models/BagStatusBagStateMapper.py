"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class BagStatusBagStateMapper(BaseSchema):
    #  swagger.json

    
    is_active = fields.Boolean(required=False)
    
    display_name = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    app_display_name = fields.Str(required=False)
    
    app_state_name = fields.Str(required=False)
    
