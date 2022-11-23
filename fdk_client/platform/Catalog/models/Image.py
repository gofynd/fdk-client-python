"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class Image(BaseSchema):
    #  swagger.json

    
    url = fields.Str(required=False)
    
    aspect_ratio_f = fields.Float(required=False)
    
    aspect_ratio = fields.Str(required=False)
    
    secure_url = fields.Str(required=False)
    
