"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










from .StoreDetail import StoreDetail







from .ProductStockPrice import ProductStockPrice



from .CompanyDetail import CompanyDetail



from .Seller import Seller



class ProductStockStatusItem(BaseSchema):
    #  swagger.json

    
    size = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    store = fields.Nested(StoreDetail, required=False)
    
    identifier = fields.Dict(required=False)
    
    item_id = fields.Int(required=False)
    
    price = fields.Nested(ProductStockPrice, required=False)
    
    company = fields.Nested(CompanyDetail, required=False)
    
    seller = fields.Nested(Seller, required=False)
    
