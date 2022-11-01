"""Configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class OrderFeature(BaseSchema):
    #  swagger.json

    
    buy_again = fields.Boolean(required=False)
    
