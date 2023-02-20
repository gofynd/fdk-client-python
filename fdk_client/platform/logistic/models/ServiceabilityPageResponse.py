"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class ServiceabilityPageResponse(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    item_total = fields.Int(required=False)
    
    current = fields.Int(required=False)
    
