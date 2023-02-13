"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class Entities(BaseSchema):
    # OrderManage swagger.json

    
    affiliate_bag_id = fields.Str(required=False)
    
    affiliate_shipment_id = fields.Str(required=False)
    
    reason_text = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    affiliate_id = fields.Str(required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
