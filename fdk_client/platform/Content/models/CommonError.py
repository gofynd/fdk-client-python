"""Content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class CommonError(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
