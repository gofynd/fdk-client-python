"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OriginalFilter import OriginalFilter











from .Bags import Bags






class CheckResponse(BaseSchema):
    # Order swagger.json

    
    original_filter = fields.Nested(OriginalFilter, required=False)
    
    is_bag_locked = fields.Boolean(required=False)
    
    shipment_id = fields.Str(required=False)
    
    affiliate_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    is_shipment_locked = fields.Boolean(required=False)
    
    bags = fields.List(fields.Nested(Bags, required=False), required=False)
    
    lock_status = fields.Boolean(required=False)
    
    affiliate_shipment_id = fields.Str(required=False)
    

