"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














from .DimensionResponse1 import DimensionResponse1







from .UserSerializer import UserSerializer



from .QuantitiesArticle import QuantitiesArticle



from .ManufacturerResponse1 import ManufacturerResponse1







from .UserSerializer import UserSerializer



from .ArticleStoreResponse import ArticleStoreResponse



from .ReturnConfig3 import ReturnConfig3



from .PriceArticle import PriceArticle



from .Trader3 import Trader3





from .WeightResponse1 import WeightResponse1







from .CompanyMeta1 import CompanyMeta1



from .DateMeta import DateMeta











from .BrandMeta1 import BrandMeta1



class GetInventories(BaseSchema):
    #  swagger.json

    
    id = fields.Str(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    total_quantity = fields.Int(required=False)
    
    identifier = fields.Dict(required=False)
    
    inventory_updated_on = fields.Str(required=False)
    
    dimension = fields.Nested(DimensionResponse1, required=False)
    
    stage = fields.Str(required=False)
    
    expiration_date = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    quantities = fields.Nested(QuantitiesArticle, required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse1, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    country_of_origin = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    store = fields.Nested(ArticleStoreResponse, required=False)
    
    return_config = fields.Nested(ReturnConfig3, required=False)
    
    price = fields.Nested(PriceArticle, required=False)
    
    trader = fields.List(fields.Nested(Trader3, required=False), required=False)
    
    platforms = fields.Dict(required=False)
    
    weight = fields.Nested(WeightResponse1, required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    size = fields.Str(required=False)
    
    company = fields.Nested(CompanyMeta1, required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    
    trace_id = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    brand = fields.Nested(BrandMeta1, required=False)
    
