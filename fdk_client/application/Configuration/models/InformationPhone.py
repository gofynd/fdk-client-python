"""Configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class InformationPhone(BaseSchema):
    #  swagger.json

    
    code = fields.Str(required=False)
    
    number = fields.Str(required=False)
    
