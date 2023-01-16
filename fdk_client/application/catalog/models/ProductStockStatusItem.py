"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .StoreDetail import StoreDetail



from .Seller import Seller











from .ProductStockPrice import ProductStockPrice



from .CompanyDetail import CompanyDetail





class ProductStockStatusItem(BaseSchema):
    #  swagger.json

    
    store = fields.Nested(StoreDetail, required=False)
    
    seller = fields.Nested(Seller, required=False)
    
    item_id = fields.Int(required=False)
    
    uid = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    price = fields.Nested(ProductStockPrice, required=False)
    
    company = fields.Nested(CompanyDetail, required=False)
    
    identifier = fields.Dict(required=False)
    