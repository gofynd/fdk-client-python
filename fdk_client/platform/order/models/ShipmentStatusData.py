"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class ShipmentStatusData(BaseSchema):
    #  swagger.json

    
    status = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    shipment_id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    bag_list = fields.List(fields.Int(required=False), required=False)
    
