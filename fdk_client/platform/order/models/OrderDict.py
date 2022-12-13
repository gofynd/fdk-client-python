"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class OrderDict(BaseSchema):
    #  swagger.json

    
    fynd_order_id = fields.Str(required=False)
    
    shipment_count = fields.Int(required=False)
    
    order_date = fields.Str(required=False)
    
