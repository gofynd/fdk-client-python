"""PosCart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class UpdateCartShipmentItem(BaseSchema):
    #  swagger.json

    
    shipment_type = fields.Str(required=False)
    
    article_uid = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
