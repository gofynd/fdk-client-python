"""Communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class PayloadEmailProviderStructure(BaseSchema):
    #  swagger.json

    
    _id = fields.Str(required=False)
    
