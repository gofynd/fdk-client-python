"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Meta import Meta













class ShipmentDetail(BaseSchema):
    #  swagger.json

    
    meta = fields.Nested(Meta, required=False)
    
    bag_list = fields.List(fields.Int(required=False), required=False)
    
    shipment_id = fields.Str(required=False)
    
    remarks = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    status = fields.Str(required=False)
    
