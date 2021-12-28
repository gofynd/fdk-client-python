"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema



from .Seller import Seller





from .ProductStockPrice import ProductStockPrice

from .StoreDetail import StoreDetail





from .CompanyDetail import CompanyDetail


class ProductStockStatusItem(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Str(required=False)
    
    seller = fields.Nested(Seller, required=False)
    
    quantity = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    price = fields.Nested(ProductStockPrice, required=False)
    
    store = fields.Nested(StoreDetail, required=False)
    
    identifier = fields.Dict(required=False)
    
    item_id = fields.Int(required=False)
    
    company = fields.Nested(CompanyDetail, required=False)
    

