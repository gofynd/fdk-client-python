"""theme Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .BlocksProps import BlocksProps



class Blocks(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    props = fields.List(fields.Nested(BlocksProps, required=False), required=False)
    
