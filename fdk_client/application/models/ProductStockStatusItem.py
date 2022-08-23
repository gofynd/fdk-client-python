"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .CompanyDetail import CompanyDetail

from .StoreDetail import StoreDetail



from .ProductStockPrice import ProductStockPrice



from .Seller import Seller




class ProductStockStatusItem(BaseSchema):
    # Catalog swagger.json

    
    quantity = fields.Int(required=False)
    
    item_id = fields.Int(required=False)
    
    company = fields.Nested(CompanyDetail, required=False)
    
    store = fields.Nested(StoreDetail, required=False)
    
    size = fields.Str(required=False)
    
    price = fields.Nested(ProductStockPrice, required=False)
    
    uid = fields.Str(required=False)
    
    seller = fields.Nested(Seller, required=False)
    
    identifier = fields.Dict(required=False)
    

