"""lead Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class SubmitButton(BaseSchema):
    #  swagger.json

    
    title = fields.Str(required=False)
    
    title_color = fields.Str(required=False)
    
    background_color = fields.Str(required=False)
    
