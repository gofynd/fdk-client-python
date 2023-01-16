"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class OrderDict(BaseSchema):
    # Order swagger.json

    
    order_date = fields.Str(required=False)
    
    fynd_order_id = fields.Str(required=False)
    
    shipment_count = fields.Int(required=False)
    

