"""Content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class SEOImage(BaseSchema):
    #  swagger.json

    
    url = fields.Str(required=False)
    
