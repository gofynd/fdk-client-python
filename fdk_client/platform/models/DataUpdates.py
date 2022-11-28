"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductsDataUpdates import ProductsDataUpdates

from .EntitiesDataUpdates import EntitiesDataUpdates


class DataUpdates(BaseSchema):
    # OrderManage swagger.json

    
    products = fields.List(fields.Nested(ProductsDataUpdates, required=False), required=False)
    
    entities = fields.List(fields.Nested(EntitiesDataUpdates, required=False), required=False)
    

