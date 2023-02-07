"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ProductStockStatusItem import ProductStockStatusItem



class ProductStockStatusResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(ProductStockStatusItem, required=False), required=False)
    
