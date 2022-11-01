"""User Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class CodeRequestBodySchema(BaseSchema):
    #  swagger.json

    
    code = fields.Str(required=False)
    
