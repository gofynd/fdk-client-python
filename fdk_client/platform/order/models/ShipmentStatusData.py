"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class ShipmentStatusData(BaseSchema):
    #  swagger.json

    
    shipment_id = fields.Str(required=False)
    
    bag_list = fields.List(fields.Str(required=False), required=False)
    
    created_at = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
