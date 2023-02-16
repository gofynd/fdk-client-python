"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class UsesRemaining1(BaseSchema):
    #  swagger.json

    
    total = fields.Int(required=False)
    
    user = fields.Int(required=False)
    
