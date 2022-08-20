"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class ShipmentStatusData(BaseSchema):
    # Orders swagger.json

    
    created_at = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    bag_list = fields.List(fields.Int(required=False), required=False)
    
    id = fields.Int(required=False)
    
    shipment_id = fields.Str(required=False)
    
