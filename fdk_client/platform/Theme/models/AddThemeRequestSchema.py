"""Theme Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class AddThemeRequestSchema(BaseSchema):
    #  swagger.json

    
    theme_id = fields.Str(required=False)
    
