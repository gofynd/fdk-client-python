"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class OrderFeature(BaseSchema):
    #  swagger.json

    
    buy_again = fields.Boolean(required=False)
    
