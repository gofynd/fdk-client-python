"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ShipmentReason import ShipmentReason



class ShipmentReasons1(BaseSchema):
    #  swagger.json

    
    reasons = fields.List(fields.Nested(ShipmentReason, required=False), required=False)
    
