"""Content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .HandpickedTagSchema import HandpickedTagSchema



class UpdateHandpickedSchema(BaseSchema):
    #  swagger.json

    
    tag = fields.Nested(HandpickedTagSchema, required=False)
    
