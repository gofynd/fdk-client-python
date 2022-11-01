"""Content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class EmailProperties(BaseSchema):
    #  swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
