"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Media import Media











class Department(BaseSchema):
    #  swagger.json

    
    logo = fields.Nested(Media, required=False)
    
    slug = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    priority_order = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    
