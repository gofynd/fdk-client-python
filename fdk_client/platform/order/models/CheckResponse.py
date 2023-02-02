"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
















from .OriginalFilter import OriginalFilter





from .Bags import Bags



class CheckResponse(BaseSchema):
    #  swagger.json

    
    affiliate_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    affiliate_shipment_id = fields.Str(required=False)
    
    lock_status = fields.Boolean(required=False)
    
    is_bag_locked = fields.Boolean(required=False)
    
    is_shipment_locked = fields.Boolean(required=False)
    
    original_filter = fields.Nested(OriginalFilter, required=False)
    
    shipment_id = fields.Str(required=False)
    
    bags = fields.List(fields.Nested(Bags, required=False), required=False)
    
