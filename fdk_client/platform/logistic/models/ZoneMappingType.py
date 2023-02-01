"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class ZoneMappingType(BaseSchema):
    #  swagger.json

    
    pincode = fields.List(fields.Str(required=False), required=False)
    
    country = fields.Str(required=False)
    
    state = fields.List(fields.Str(required=False), required=False)
    
