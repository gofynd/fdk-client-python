"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class IntegrationTypeResponse(BaseSchema):
    #  swagger.json

    
    order = fields.Str(required=False)
    
    inventory = fields.Str(required=False)
    
