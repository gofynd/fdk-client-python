"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class ManualAssignDPToShipment(BaseSchema):
    # Order swagger.json

    
    qc_required = fields.Str(required=False)
    
    shipment_ids = fields.List(fields.Str(required=False), required=False)
    
    order_type = fields.Str(required=False)
    
    dp_id = fields.Int(required=False)
    

