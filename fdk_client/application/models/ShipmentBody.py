"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ProductDetail import ProductDetail








class ShipmentBody(BaseSchema):
    # Order swagger.json

    
    store_invoice_id = fields.Str(required=False)
    
    products = fields.List(fields.Nested(ProductDetail, required=False), required=False)
    
    data_update = fields.Dict(required=False)
    
    bags = fields.List(fields.Int(required=False), required=False)
    
    reason = fields.List(fields.Int(required=False), required=False)
    
