"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Shipments import Shipments



class ShipmentById(BaseSchema):
    #  swagger.json

    
    shipment = fields.Nested(Shipments, required=False)
    
