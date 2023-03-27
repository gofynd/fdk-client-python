"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductSizePriceResponseV3 import ProductSizePriceResponseV3

from .ProductSizeSellerFilterSchemaV3 import ProductSizeSellerFilterSchemaV3

from .Page import Page


class ProductSizeSellersResponseV3(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(ProductSizePriceResponseV3, required=False), required=False)
    
    sort_on = fields.List(fields.Nested(ProductSizeSellerFilterSchemaV3, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

