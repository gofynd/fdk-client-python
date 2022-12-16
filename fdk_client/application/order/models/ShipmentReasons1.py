"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Reasons import Reasons



class ShipmentReasons1(BaseSchema):
    #  swagger.json

    
    reasons = fields.List(fields.Nested(Reasons, required=False), required=False)
    