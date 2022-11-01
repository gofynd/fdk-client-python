"""Rewards Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class Points(BaseSchema):
    #  swagger.json

    
    available = fields.Float(required=False)
    
