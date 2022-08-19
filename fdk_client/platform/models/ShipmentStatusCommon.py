"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
















class ShipmentStatusCommon(BaseSchema):
    # Order swagger.json

    
    created_at = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    bag_list = fields.List(fields.Str(required=False), required=False)
    
    ss_id = fields.Int(required=False)
    
    current_shipment_status = fields.Str(required=False)
    
    status_created_at = fields.Str(required=False)
    

