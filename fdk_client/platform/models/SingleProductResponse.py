"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Product import Product


class SingleProductResponse(BaseSchema):
    # Catalog swagger.json

    
    data = fields.Nested(Product, required=False)
    

