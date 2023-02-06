"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class IntegrationTypeResponse(BaseSchema):
    #  swagger.json

    
    inventory = fields.Str(required=False)
    
    order = fields.Str(required=False)
    
