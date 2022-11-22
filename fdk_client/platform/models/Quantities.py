"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .QuantityBase import QuantityBase

from .QuantityBase import QuantityBase

from .QuantityBase import QuantityBase

from .QuantityBase import QuantityBase


class Quantities(BaseSchema):
    # Catalog swagger.json

    
    order_committed = fields.Nested(QuantityBase, required=False)
    
    damaged = fields.Nested(QuantityBase, required=False)
    
    not_available = fields.Nested(QuantityBase, required=False)
    
    sellable = fields.Nested(QuantityBase, required=False)
    

