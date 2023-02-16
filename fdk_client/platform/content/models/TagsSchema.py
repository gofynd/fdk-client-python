"""content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .TagSchema import TagSchema



class TagsSchema(BaseSchema):
    #  swagger.json

    
    application = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    tags = fields.List(fields.Nested(TagSchema, required=False), required=False)
    
