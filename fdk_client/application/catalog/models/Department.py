"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










from .Media import Media





class Department(BaseSchema):
    #  swagger.json

    
    priority_order = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    name = fields.Str(required=False)
    
