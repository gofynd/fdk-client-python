"""Theme Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class BlitzkriegNotFoundSchema(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
