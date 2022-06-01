"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Seller import Seller



from .CompanyDetail import CompanyDetail







from .StoreDetail import StoreDetail



from .ProductStockPrice import ProductStockPrice


class ProductStockStatusItem(BaseSchema):
    # Catalog swagger.json

    
    seller = fields.Nested(Seller, required=False)
    
    identifier = fields.Dict(required=False)
    
    company = fields.Nested(CompanyDetail, required=False)
    
    size = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    item_id = fields.Int(required=False)
    
    store = fields.Nested(StoreDetail, required=False)
    
    uid = fields.Str(required=False)
    
    price = fields.Nested(ProductStockPrice, required=False)
    

