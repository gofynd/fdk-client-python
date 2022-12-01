"""configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .OS import OS



class Device(BaseSchema):
    #  swagger.json

    
    build = fields.Int(required=False)
    
    model = fields.Str(required=False)
    
    os = fields.Nested(OS, required=False)
    
