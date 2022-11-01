"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class Damaged(BaseSchema):
    #  swagger.json

    
    updated_at = fields.Str(required=False)
    
    count = fields.Int(required=False)
    
