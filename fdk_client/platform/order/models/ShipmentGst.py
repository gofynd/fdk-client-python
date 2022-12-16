"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class ShipmentGst(BaseSchema):
    #  swagger.json

    
    brand_calculated_amount = fields.Float(required=False)
    
    value_of_good = fields.Float(required=False)
    
    gst_fee = fields.Float(required=False)
    