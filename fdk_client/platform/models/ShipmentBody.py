"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ProductDetail import ProductDetail




class ShipmentBody(BaseSchema):
    # OrderManage swagger.json

    
    reason = fields.List(fields.Int(required=False), required=False)
    
    data_update = fields.Dict(required=False)
    
    products = fields.List(fields.Nested(ProductDetail, required=False), required=False)
    
    store_invoice_id = fields.Str(required=False)
    
