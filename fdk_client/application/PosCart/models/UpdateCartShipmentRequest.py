"""PosCart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .UpdateCartShipmentItem import UpdateCartShipmentItem



class UpdateCartShipmentRequest(BaseSchema):
    #  swagger.json

    
    shipments = fields.List(fields.Nested(UpdateCartShipmentItem, required=False), required=False)
    
