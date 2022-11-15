"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .SizeDistribution import SizeDistribution



class InventorySet(BaseSchema):
    #  swagger.json

    
    quantity = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    size_distribution = fields.Nested(SizeDistribution, required=False)
    
