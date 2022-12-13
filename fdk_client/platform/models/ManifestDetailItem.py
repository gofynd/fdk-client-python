"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class ManifestDetailItem(BaseSchema):
    # Order swagger.json

    
    invoice_id = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    awb = fields.Str(required=False)
    
    item_qty = fields.Int(required=False)
    
    shipment_id = fields.Str(required=False)
    

