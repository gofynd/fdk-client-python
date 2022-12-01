"""content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class SEOImage(BaseSchema):
    #  swagger.json

    
    url = fields.Str(required=False)
    
