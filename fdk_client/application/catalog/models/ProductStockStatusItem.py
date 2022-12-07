"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .CompanyDetail import CompanyDetail



from .Seller import Seller





from .ProductStockPrice import ProductStockPrice





from .StoreDetail import StoreDetail







class ProductStockStatusItem(BaseSchema):
    #  swagger.json

    
    uid = fields.Str(required=False)
    
    company = fields.Nested(CompanyDetail, required=False)
    
    seller = fields.Nested(Seller, required=False)
    
    identifier = fields.Dict(required=False)
    
    price = fields.Nested(ProductStockPrice, required=False)
    
    item_id = fields.Int(required=False)
    
    store = fields.Nested(StoreDetail, required=False)
    
    size = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
