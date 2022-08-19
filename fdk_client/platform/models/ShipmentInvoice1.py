"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class ShipmentInvoice1(BaseSchema):
    # Order swagger.json

    
    updated_date = fields.Int(required=False)
    
    store_invoice_id = fields.Str(required=False)
    
    invoice_url = fields.Str(required=False)
    
    label_url = fields.Str(required=False)
    

