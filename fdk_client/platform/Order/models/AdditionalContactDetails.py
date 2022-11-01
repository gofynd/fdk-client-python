"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class AdditionalContactDetails(BaseSchema):
    #  swagger.json

    
    number = fields.List(fields.Str(required=False), required=False)
    
