"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CompanyDetail import CompanyDetail







from .ProductStockPrice import ProductStockPrice

from .Seller import Seller



from .StoreDetail import StoreDetail




class ProductStockStatusItem(BaseSchema):
    # Catalog swagger.json

    
    company = fields.Nested(CompanyDetail, required=False)
    
    identifier = fields.Dict(required=False)
    
    quantity = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    price = fields.Nested(ProductStockPrice, required=False)
    
    seller = fields.Nested(Seller, required=False)
    
    item_id = fields.Int(required=False)
    
    store = fields.Nested(StoreDetail, required=False)
    
    uid = fields.Str(required=False)
    

