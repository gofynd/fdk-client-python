"""theme Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema
















class Colors(BaseSchema):
    #  swagger.json

    
    bg_color = fields.Str(required=False)
    
    primary_color = fields.Str(required=False)
    
    secondary_color = fields.Str(required=False)
    
    accent_color = fields.Str(required=False)
    
    link_color = fields.Str(required=False)
    
    button_secondary_color = fields.Str(required=False)
    
