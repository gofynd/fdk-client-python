"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Page import Page

from .ProductVariants import ProductVariants


class ProductVariantsResponse(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    variants = fields.List(fields.Nested(ProductVariants, required=False), required=False)
    

