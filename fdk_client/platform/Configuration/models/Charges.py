"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class Charges(BaseSchema):
    #  swagger.json

    
    threshold = fields.Float(required=False)
    
    charges = fields.Float(required=False)
    
