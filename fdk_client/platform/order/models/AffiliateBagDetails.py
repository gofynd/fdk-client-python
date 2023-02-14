"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .AffiliateMeta import AffiliateMeta











class AffiliateBagDetails(BaseSchema):
    #  swagger.json

    
    affiliate_meta = fields.Nested(AffiliateMeta, required=False)
    
    employee_discount = fields.Float(required=False)
    
    affiliate_bag_id = fields.Str(required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    loyalty_discount = fields.Float(required=False)
    
