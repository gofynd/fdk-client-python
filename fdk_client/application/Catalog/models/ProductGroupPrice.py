"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class ProductGroupPrice(BaseSchema):
    #  swagger.json

    
    max_marked = fields.Float(required=False)
    
    min_marked = fields.Float(required=False)
    
    max_effective = fields.Float(required=False)
    
    min_effective = fields.Float(required=False)
    
    currency = fields.Raw(required=False)
    
