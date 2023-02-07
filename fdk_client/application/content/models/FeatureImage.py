"""content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class FeatureImage(BaseSchema):
    #  swagger.json

    
    secure_url = fields.Str(required=False)
    
