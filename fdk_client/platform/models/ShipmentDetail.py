"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Meta1 import Meta1










class ShipmentDetail(BaseSchema):
    # Order swagger.json

    
    bag_list = fields.List(fields.Int(required=False), required=False)
    
    meta = fields.Nested(Meta1, required=False)
    
    remarks = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    status = fields.Str(required=False)
    

