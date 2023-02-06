"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class ShipmentStatus(BaseSchema):
    #  swagger.json

    
    title = fields.Str(required=False)
    
    hex_code = fields.Str(required=False)
    
