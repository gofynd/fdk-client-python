"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class ShipmentUpdateRequest(BaseSchema):
    #  swagger.json

    
    bags = fields.List(fields.Str(required=False), required=False)
    
    reason = fields.Dict(required=False)
    
    comments = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
