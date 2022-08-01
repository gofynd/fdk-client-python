"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Price import Price

from .Size import Size











from .LimitedProductData import LimitedProductData




class GetProducts(BaseSchema):
    # Catalog swagger.json

    
    price = fields.Nested(Price, required=False)
    
    sizes = fields.List(fields.Nested(Size, required=False), required=False)
    
    min_quantity = fields.Int(required=False)
    
    auto_add_to_cart = fields.Boolean(required=False)
    
    allow_remove = fields.Boolean(required=False)
    
    max_quantity = fields.Int(required=False)
    
    auto_select = fields.Boolean(required=False)
    
    product_details = fields.Nested(LimitedProductData, required=False)
    
    product_uid = fields.Int(required=False)
    

