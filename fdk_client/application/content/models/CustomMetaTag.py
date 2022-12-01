"""content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class CustomMetaTag(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    content = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
