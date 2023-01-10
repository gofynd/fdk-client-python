"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class UpdateShipmentExternalRequest(BaseSchema):
    #  swagger.json

    
    statuses = fields.List(fields.Dict(required=False), required=False)
    
    force_transition = fields.Boolean(required=False)
    
