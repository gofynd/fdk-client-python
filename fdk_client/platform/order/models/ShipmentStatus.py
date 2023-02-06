"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class ShipmentStatus(BaseSchema):
    #  swagger.json

    
    title = fields.Str(required=False)
    
    ops_status = fields.Str(required=False)
    
    hex_code = fields.Str(required=False)
    
    actual_status = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
