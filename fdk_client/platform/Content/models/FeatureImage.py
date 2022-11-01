"""Content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class FeatureImage(BaseSchema):
    #  swagger.json

    
    secure_url = fields.Str(required=False)
    
