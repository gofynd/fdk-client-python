"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductSizePriceResponse import ProductSizePriceResponse

from .Page import Page

from .ProductSizeSellerFilter import ProductSizeSellerFilter


class ProductSizeSellersResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(ProductSizePriceResponse, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    sort_on = fields.List(fields.Nested(ProductSizeSellerFilter, required=False), required=False)
    

