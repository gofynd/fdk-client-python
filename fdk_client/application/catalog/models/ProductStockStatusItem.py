"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Seller import Seller





from .StoreDetail import StoreDetail









from .CompanyDetail import CompanyDetail





from .ProductStockPrice import ProductStockPrice



class ProductStockStatusItem(BaseSchema):
    #  swagger.json

    
    seller = fields.Nested(Seller, required=False)
    
    identifier = fields.Dict(required=False)
    
    store = fields.Nested(StoreDetail, required=False)
    
    quantity = fields.Int(required=False)
    
    item_id = fields.Int(required=False)
    
    uid = fields.Str(required=False)
    
    company = fields.Nested(CompanyDetail, required=False)
    
    size = fields.Str(required=False)
    
    price = fields.Nested(ProductStockPrice, required=False)
    
