"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class ShipmentStatusUpdate(BaseSchema):
    #  swagger.json

    
    message = fields.List(fields.Dict(required=False), required=False)
    
    status = fields.Boolean(required=False)
    
