"""Content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class RemoveHandpickedSchema(BaseSchema):
    #  swagger.json

    
    tags = fields.List(fields.Str(required=False), required=False)
    
