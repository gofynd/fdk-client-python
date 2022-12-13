"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .Meta import Meta


class ShipmentDetail(BaseSchema):
    # Order swagger.json

    
    status = fields.Str(required=False)
    
    remarks = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    bag_list = fields.List(fields.Int(required=False), required=False)
    
    id = fields.Int(required=False)
    
    meta = fields.Nested(Meta, required=False)
    

