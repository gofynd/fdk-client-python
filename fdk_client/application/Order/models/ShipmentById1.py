"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Shipments1 import Shipments1



class ShipmentById1(BaseSchema):
    #  swagger.json

    
    shipment = fields.Nested(Shipments1, required=False)
    
