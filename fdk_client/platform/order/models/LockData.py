"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class LockData(BaseSchema):
    #  swagger.json

    
    locked = fields.Boolean(required=False)
    
    lock_message = fields.Str(required=False)
    
    mto = fields.Boolean(required=False)
    
