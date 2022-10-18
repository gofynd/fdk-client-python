"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class ShipmentEDDUpdate(BaseSchema):
    # OrderManage swagger.json

    
    edd = fields.Str(required=False)
    
    reason_text = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    reason_id = fields.List(fields.Int(required=False), required=False)
    

