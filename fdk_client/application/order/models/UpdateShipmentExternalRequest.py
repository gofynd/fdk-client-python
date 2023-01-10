"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class UpdateShipmentExternalRequest(BaseSchema):
    #  swagger.json

    
    force_transition = fields.Boolean(required=False)
    
    statuses = fields.List(fields.Dict(required=False), required=False)
    
