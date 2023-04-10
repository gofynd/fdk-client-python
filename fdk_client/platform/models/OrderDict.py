"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .OrderMeta import OrderMeta





from .Prices import Prices

from .TaxDetails import TaxDetails


class OrderDict(BaseSchema):
    # Order swagger.json

    
    order_date = fields.Str(required=False)
    
    meta = fields.Nested(OrderMeta, required=False)
    
    fynd_order_id = fields.Str(required=False)
    
    payment_methods = fields.Dict(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    tax_details = fields.Nested(TaxDetails, required=False)
    

