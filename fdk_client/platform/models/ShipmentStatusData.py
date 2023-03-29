"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class ShipmentStatusData(BaseSchema):
    # Order swagger.json

    
    created_at = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    bag_list = fields.List(fields.Str(required=False), required=False)
    

