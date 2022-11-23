"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Price1 import Price1



from .Price1 import Price1



class ProductListingPrice(BaseSchema):
    #  swagger.json

    
    effective = fields.Nested(Price1, required=False)
    
    marked = fields.Nested(Price1, required=False)
    
