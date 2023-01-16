"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class PageResponseType(BaseSchema):
    #  swagger.json

    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    next = fields.Int(required=False)
    
    total_count = fields.Int(required=False)
    