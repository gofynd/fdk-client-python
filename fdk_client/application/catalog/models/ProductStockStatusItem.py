"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .CompanyDetail import CompanyDetail



from .ProductStockPrice import ProductStockPrice





from .Seller import Seller



from .StoreDetail import StoreDetail











class ProductStockStatusItem(BaseSchema):
    #  swagger.json

    
    company = fields.Nested(CompanyDetail, required=False)
    
    price = fields.Nested(ProductStockPrice, required=False)
    
    size = fields.Str(required=False)
    
    seller = fields.Nested(Seller, required=False)
    
    store = fields.Nested(StoreDetail, required=False)
    
    uid = fields.Str(required=False)
    
    identifier = fields.Dict(required=False)
    
    item_id = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
