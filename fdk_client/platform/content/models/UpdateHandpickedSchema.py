"""content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .HandpickedTagSchema import HandpickedTagSchema



class UpdateHandpickedSchema(BaseSchema):
    #  swagger.json

    
    tag = fields.Nested(HandpickedTagSchema, required=False)
    
