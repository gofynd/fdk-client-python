"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class HomePageFeature(BaseSchema):
    #  swagger.json

    
    order_processing = fields.Boolean(required=False)
    
