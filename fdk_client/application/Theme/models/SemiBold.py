"""Theme Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class SemiBold(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    file = fields.Str(required=False)
    
