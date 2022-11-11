"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .BagReasons import BagReasons



class ShipmentBagReasons(BaseSchema):
    #  swagger.json

    
    reasons = fields.List(fields.Nested(BagReasons, required=False), required=False)
    
