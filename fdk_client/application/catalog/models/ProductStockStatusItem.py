"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .CompanyDetail import CompanyDetail





from .Seller import Seller





from .StoreDetail import StoreDetail









from .ProductStockPrice import ProductStockPrice



class ProductStockStatusItem(BaseSchema):
    #  swagger.json

    
    company = fields.Nested(CompanyDetail, required=False)
    
    uid = fields.Str(required=False)
    
    seller = fields.Nested(Seller, required=False)
    
    quantity = fields.Int(required=False)
    
    store = fields.Nested(StoreDetail, required=False)
    
    size = fields.Str(required=False)
    
    identifier = fields.Dict(required=False)
    
    item_id = fields.Int(required=False)
    
    price = fields.Nested(ProductStockPrice, required=False)
    
