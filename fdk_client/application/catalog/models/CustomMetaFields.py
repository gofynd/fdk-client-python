"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class CustomMetaFields(BaseSchema):
    #  swagger.json

    
    value = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
