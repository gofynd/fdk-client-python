"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class CartFeature(BaseSchema):
    #  swagger.json

    
    gst_input = fields.Boolean(required=False)
    
    staff_selection = fields.Boolean(required=False)
    
    placing_for_customer = fields.Boolean(required=False)
    
    google_map = fields.Boolean(required=False)
    
    revenue_engine_coupon = fields.Boolean(required=False)
    
