"""discount Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class ValidityObject(BaseSchema):
    #  swagger.json

    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    