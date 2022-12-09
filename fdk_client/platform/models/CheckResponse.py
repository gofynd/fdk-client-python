"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Bags import Bags













from .OriginalFilter import OriginalFilter




class CheckResponse(BaseSchema):
    # OrderManage swagger.json

    
    bags = fields.List(fields.Nested(Bags, required=False), required=False)
    
    status = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    is_shipment_locked = fields.Boolean(required=False)
    
    lock_status = fields.Boolean(required=False)
    
    is_bag_locked = fields.Boolean(required=False)
    
    affiliate_id = fields.Str(required=False)
    
    original_filter = fields.Nested(OriginalFilter, required=False)
    
    affiliate_shipment_id = fields.Str(required=False)
    

