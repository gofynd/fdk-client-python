"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class ZoneProductTypes(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
