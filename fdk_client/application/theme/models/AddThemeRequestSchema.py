"""theme Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class AddThemeRequestSchema(BaseSchema):
    #  swagger.json

    
    theme_id = fields.Str(required=False)
    
