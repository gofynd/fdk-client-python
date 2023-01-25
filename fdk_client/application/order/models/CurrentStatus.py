"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class CurrentStatus(BaseSchema):
    #  swagger.json

    
    journey_type = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
