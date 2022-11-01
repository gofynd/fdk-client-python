"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class CrossSellingData(BaseSchema):
    #  swagger.json

    
    articles = fields.Int(required=False)
    
    products = fields.Int(required=False)
    
