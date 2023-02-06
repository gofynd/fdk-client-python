"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class StageItem(BaseSchema):
    #  swagger.json

    
    count = fields.Int(required=False)
    
    text = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
