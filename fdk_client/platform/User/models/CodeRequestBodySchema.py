"""User Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class CodeRequestBodySchema(BaseSchema):
    #  swagger.json

    
    code = fields.Str(required=False)
    
