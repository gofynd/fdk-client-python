"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ShipmentResponse import ShipmentResponse



class ShipmentById1(BaseSchema):
    #  swagger.json

    
    shipment = fields.Nested(ShipmentResponse, required=False)
    
