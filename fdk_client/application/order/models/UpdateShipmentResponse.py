"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class UpdateShipmentResponse(BaseSchema):
    #  swagger.json

    
    final_state = fields.Dict(required=False)
    
    status = fields.Boolean(required=False)
    
    message = fields.List(fields.Str(required=False), required=False)
    
