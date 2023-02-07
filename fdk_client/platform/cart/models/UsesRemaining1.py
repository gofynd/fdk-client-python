"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class UsesRemaining1(BaseSchema):
    #  swagger.json

    
    user = fields.Int(required=False)
    
    total = fields.Int(required=False)
    
