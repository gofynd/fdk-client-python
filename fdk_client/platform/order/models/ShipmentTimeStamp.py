"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class ShipmentTimeStamp(BaseSchema):
    #  swagger.json

    
    t_min = fields.Str(required=False)
    
    t_max = fields.Str(required=False)
    
