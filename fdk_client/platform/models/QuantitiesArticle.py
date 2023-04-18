"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Quantity import Quantity

from .Quantity import Quantity

from .Quantity import Quantity

from .Quantity import Quantity


class QuantitiesArticle(BaseSchema):
    # Catalog swagger.json

    
    not_available = fields.Nested(Quantity, required=False)
    
    sellable = fields.Nested(Quantity, required=False)
    
    damaged = fields.Nested(Quantity, required=False)
    
    order_committed = fields.Nested(Quantity, required=False)
    

