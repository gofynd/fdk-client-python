"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










from .ProductStockPrice import ProductStockPrice



from .Seller import Seller





from .StoreDetail import StoreDetail





from .CompanyDetail import CompanyDetail



class ProductStockStatusItem(BaseSchema):
    #  swagger.json

    
    identifier = fields.Dict(required=False)
    
    quantity = fields.Int(required=False)
    
    uid = fields.Str(required=False)
    
    price = fields.Nested(ProductStockPrice, required=False)
    
    seller = fields.Nested(Seller, required=False)
    
    item_id = fields.Int(required=False)
    
    store = fields.Nested(StoreDetail, required=False)
    
    size = fields.Str(required=False)
    
    company = fields.Nested(CompanyDetail, required=False)
    
