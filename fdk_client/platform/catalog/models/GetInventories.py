"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ArticleStoreResponse import ArticleStoreResponse











from .PriceArticle import PriceArticle







from .BrandMeta1 import BrandMeta1



from .DateMeta import DateMeta



from .WeightResponse1 import WeightResponse1







from .DimensionResponse1 import DimensionResponse1





from .ManufacturerResponse1 import ManufacturerResponse1





from .ReturnConfig4 import ReturnConfig4



from .UserSerializer import UserSerializer





from .UserSerializer import UserSerializer







from .QuantitiesArticle import QuantitiesArticle





from .CompanyMeta1 import CompanyMeta1







from .Trader3 import Trader3



class GetInventories(BaseSchema):
    #  swagger.json

    
    store = fields.Nested(ArticleStoreResponse, required=False)
    
    country_of_origin = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    size = fields.Str(required=False)
    
    price = fields.Nested(PriceArticle, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    stage = fields.Str(required=False)
    
    brand = fields.Nested(BrandMeta1, required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    
    weight = fields.Nested(WeightResponse1, required=False)
    
    trace_id = fields.Str(required=False)
    
    expiration_date = fields.Str(required=False)
    
    dimension = fields.Nested(DimensionResponse1, required=False)
    
    identifier = fields.Dict(required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse1, required=False)
    
    total_quantity = fields.Int(required=False)
    
    return_config = fields.Nested(ReturnConfig4, required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    uid = fields.Str(required=False)
    
    inventory_updated_on = fields.Str(required=False)
    
    quantities = fields.Nested(QuantitiesArticle, required=False)
    
    platforms = fields.Dict(required=False)
    
    company = fields.Nested(CompanyMeta1, required=False)
    
    id = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    trader = fields.List(fields.Nested(Trader3, required=False), required=False)
    
