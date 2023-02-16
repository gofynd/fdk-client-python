"""content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .CreateTagSchema import CreateTagSchema



class CreateTagRequestSchema(BaseSchema):
    #  swagger.json

    
    tags = fields.List(fields.Nested(CreateTagSchema, required=False), required=False)
    
