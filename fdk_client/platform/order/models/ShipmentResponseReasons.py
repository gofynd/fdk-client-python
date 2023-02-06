"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class ShipmentResponseReasons(BaseSchema):
    #  swagger.json

    
    reason_id = fields.Float(required=False)
    
    reason = fields.Str(required=False)
    
