"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class Logo(BaseSchema):
    #  swagger.json

    
    secure_url = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    aspect_ratio_f = fields.Int(required=False)
    
    aspect_ratio = fields.Str(required=False)
    
