"""communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class EmailProviderReqFrom(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    
