"""Configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class HomePageFeature(BaseSchema):
    #  swagger.json

    
    order_processing = fields.Boolean(required=False)
    
