"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ShipmentConfig import ShipmentConfig



class ShipmentData(BaseSchema):
    #  swagger.json

    
    shipment_data = fields.Nested(ShipmentConfig, required=False)
    
