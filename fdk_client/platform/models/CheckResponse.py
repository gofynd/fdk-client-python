"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .OriginalFilter import OriginalFilter





from .Bags1 import Bags1










class CheckResponse(BaseSchema):
    # Order swagger.json

    
    is_bag_locked = fields.Boolean(required=False)
    
    original_filter = fields.Nested(OriginalFilter, required=False)
    
    shipment_id = fields.Str(required=False)
    
    affiliate_id = fields.Str(required=False)
    
    bags = fields.List(fields.Nested(Bags1, required=False), required=False)
    
    is_shipment_locked = fields.Boolean(required=False)
    
    affiliate_shipment_id = fields.Str(required=False)
    
    lock_status = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    
