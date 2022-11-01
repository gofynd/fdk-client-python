"""Theme Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class Css(BaseSchema):
    #  swagger.json

    
    link = fields.Str(required=False)
    
    links = fields.List(fields.Str(required=False), required=False)
    
