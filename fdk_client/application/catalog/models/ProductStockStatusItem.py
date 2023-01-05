"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ProductStockPrice import ProductStockPrice





from .CompanyDetail import CompanyDetail



from .StoreDetail import StoreDetail









from .Seller import Seller





class ProductStockStatusItem(BaseSchema):
    #  swagger.json

    
    price = fields.Nested(ProductStockPrice, required=False)
    
    size = fields.Str(required=False)
    
    company = fields.Nested(CompanyDetail, required=False)
    
    store = fields.Nested(StoreDetail, required=False)
    
    quantity = fields.Int(required=False)
    
    item_id = fields.Int(required=False)
    
    uid = fields.Str(required=False)
    
    seller = fields.Nested(Seller, required=False)
    
    identifier = fields.Dict(required=False)
    
