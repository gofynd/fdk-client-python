"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class UpdateCartShipmentItem(BaseSchema):
    #  swagger.json

    
    quantity = fields.Int(required=False)
    
    article_uid = fields.Str(required=False)
    
    shipment_type = fields.Str(required=False)
    
