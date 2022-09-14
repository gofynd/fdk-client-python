"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .StoreDetail import StoreDetail

from .ProductStockPrice import ProductStockPrice



from .Seller import Seller

from .CompanyDetail import CompanyDetail




class ProductStockStatusItem(BaseSchema):
    # Catalog swagger.json

    
    identifier = fields.Dict(required=False)
    
    item_id = fields.Int(required=False)
    
    uid = fields.Str(required=False)
    
    store = fields.Nested(StoreDetail, required=False)
    
    price = fields.Nested(ProductStockPrice, required=False)
    
    quantity = fields.Int(required=False)
    
    seller = fields.Nested(Seller, required=False)
    
    company = fields.Nested(CompanyDetail, required=False)
    
    size = fields.Str(required=False)
    

