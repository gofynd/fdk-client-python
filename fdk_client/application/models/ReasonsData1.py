"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .EntitiesReasons1 import EntitiesReasons1

from .ProductsReasons1 import ProductsReasons1


class ReasonsData1(BaseSchema):
    # Order swagger.json

    
    entities = fields.List(fields.Nested(EntitiesReasons1, required=False), required=False)
    
    products = fields.List(fields.Nested(ProductsReasons1, required=False), required=False)
    

