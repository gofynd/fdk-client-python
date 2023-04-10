"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class B2BPODetails(BaseSchema):
    # Order swagger.json

    
    partial_can_ret = fields.Boolean(required=False)
    
    item_base_price = fields.Float(required=False)
    
    po_line_amount = fields.Float(required=False)
    
    po_tax_amount = fields.Float(required=False)
    
    docker_number = fields.Str(required=False)
    
    total_gst_percentage = fields.Float(required=False)
    

