"""content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class EditorMeta(BaseSchema):
    #  swagger.json

    
    foreground_color = fields.Str(required=False)
    
    background_color = fields.Str(required=False)
    
    content_type = fields.Str(required=False)
    
    content = fields.Str(required=False)
    
