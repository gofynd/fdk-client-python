"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .BagReasons1 import BagReasons1





class ShipmentBagReasons1(BaseSchema):
    #  swagger.json

    
    reasons = fields.List(fields.Nested(BagReasons1, required=False), required=False)
    
    success = fields.Boolean(required=False)
    
