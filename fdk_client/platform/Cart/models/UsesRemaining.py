"""Cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class UsesRemaining(BaseSchema):
    #  swagger.json

    
    total = fields.Int(required=False)
    
    app = fields.Int(required=False)
    
    user = fields.Int(required=False)
    
