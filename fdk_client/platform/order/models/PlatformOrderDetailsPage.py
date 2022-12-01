"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class PlatformOrderDetailsPage(BaseSchema):
    #  swagger.json

    
    next = fields.Str(required=False)
    
    previous = fields.Str(required=False)
    
