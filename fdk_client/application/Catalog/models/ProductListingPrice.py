"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Price import Price



from .Price import Price



class ProductListingPrice(BaseSchema):
    #  swagger.json

    
    marked = fields.Nested(Price, required=False)
    
    effective = fields.Nested(Price, required=False)
    
