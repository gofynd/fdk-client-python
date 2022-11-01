"""Cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .UsesRemaining1 import UsesRemaining1



from .UsesRemaining1 import UsesRemaining1



class UsesRestriction1(BaseSchema):
    #  swagger.json

    
    maximum = fields.Nested(UsesRemaining1, required=False)
    
    remaining = fields.Nested(UsesRemaining1, required=False)
    
