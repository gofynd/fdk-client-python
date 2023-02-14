"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .WeightResponse1 import WeightResponse1







from .DimensionResponse1 import DimensionResponse1





from .ManufacturerResponse1 import ManufacturerResponse1









from .Trader3 import Trader3





from .ArticleStoreResponse import ArticleStoreResponse







from .UserSerializer import UserSerializer





from .ReturnConfig3 import ReturnConfig3





from .CompanyMeta1 import CompanyMeta1



from .QuantitiesArticle import QuantitiesArticle







from .UserSerializer import UserSerializer





from .DateMeta import DateMeta







from .BrandMeta1 import BrandMeta1



from .PriceArticle import PriceArticle





class GetInventories(BaseSchema):
    #  swagger.json

    
    weight = fields.Nested(WeightResponse1, required=False)
    
    size = fields.Str(required=False)
    
    inventory_updated_on = fields.Str(required=False)
    
    dimension = fields.Nested(DimensionResponse1, required=False)
    
    id = fields.Str(required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse1, required=False)
    
    stage = fields.Str(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    is_set = fields.Boolean(required=False)
    
    trader = fields.List(fields.Nested(Trader3, required=False), required=False)
    
    platforms = fields.Dict(required=False)
    
    store = fields.Nested(ArticleStoreResponse, required=False)
    
    trace_id = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    item_id = fields.Int(required=False)
    
    return_config = fields.Nested(ReturnConfig3, required=False)
    
    country_of_origin = fields.Str(required=False)
    
    company = fields.Nested(CompanyMeta1, required=False)
    
    quantities = fields.Nested(QuantitiesArticle, required=False)
    
    identifier = fields.Dict(required=False)
    
    total_quantity = fields.Int(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    uid = fields.Str(required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    
    expiration_date = fields.Str(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    brand = fields.Nested(BrandMeta1, required=False)
    
    price = fields.Nested(PriceArticle, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
