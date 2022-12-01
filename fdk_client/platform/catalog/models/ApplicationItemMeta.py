"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .MetaFields import MetaFields





class ApplicationItemMeta(BaseSchema):
    #  swagger.json

    
    _custom_meta = fields.List(fields.Nested(MetaFields, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
