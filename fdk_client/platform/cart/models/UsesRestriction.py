"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .UsesRemaining import UsesRemaining



from .UsesRemaining import UsesRemaining



class UsesRestriction(BaseSchema):
    #  swagger.json

    
    remaining = fields.Nested(UsesRemaining, required=False)
    
    maximum = fields.Nested(UsesRemaining, required=False)
    