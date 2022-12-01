"""content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






















from .TagSourceSchema import TagSourceSchema



class TagSchema(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    position = fields.Str(required=False)
    
    attributes = fields.Dict(required=False)
    
    content = fields.Str(required=False)
    
    pages = fields.List(fields.Dict(required=False), required=False)
    
    __source = fields.Nested(TagSourceSchema, required=False)
    
