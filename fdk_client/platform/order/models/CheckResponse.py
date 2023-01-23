"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .Bags import Bags



from .OriginalFilter import OriginalFilter













class CheckResponse(BaseSchema):
    #  swagger.json

    
    shipment_id = fields.Str(required=False)
    
    affiliate_shipment_id = fields.Str(required=False)
    
    bags = fields.List(fields.Nested(Bags, required=False), required=False)
    
    original_filter = fields.Nested(OriginalFilter, required=False)
    
    affiliate_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    lock_status = fields.Boolean(required=False)
    
    is_shipment_locked = fields.Boolean(required=False)
    
    is_bag_locked = fields.Boolean(required=False)
    
