"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .WeightResponse1 import WeightResponse1





from .ManufacturerResponse1 import ManufacturerResponse1

from .DimensionResponse1 import DimensionResponse1



from .PriceArticle import PriceArticle

from .Trader2 import Trader2





from .DateMeta import DateMeta



from .CompanyMeta1 import CompanyMeta1











from .UserSerializer import UserSerializer

from .ReturnConfig2 import ReturnConfig2



from .QuantitiesArticle import QuantitiesArticle





from .BrandMeta1 import BrandMeta1

from .UserSerializer import UserSerializer





from .ArticleStoreResponse import ArticleStoreResponse


class GetInventories(BaseSchema):
    # Catalog swagger.json

    
    country_of_origin = fields.Str(required=False)
    
    weight = fields.Nested(WeightResponse1, required=False)
    
    stage = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse1, required=False)
    
    dimension = fields.Nested(DimensionResponse1, required=False)
    
    trace_id = fields.Str(required=False)
    
    price = fields.Nested(PriceArticle, required=False)
    
    trader = fields.List(fields.Nested(Trader2, required=False), required=False)
    
    platforms = fields.Dict(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    company = fields.Nested(CompanyMeta1, required=False)
    
    size = fields.Str(required=False)
    
    inventory_updated_on = fields.Str(required=False)
    
    total_quantity = fields.Int(required=False)
    
    expiration_date = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    return_config = fields.Nested(ReturnConfig2, required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    quantities = fields.Nested(QuantitiesArticle, required=False)
    
    id = fields.Str(required=False)
    
    identifier = fields.Dict(required=False)
    
    brand = fields.Nested(BrandMeta1, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    item_id = fields.Int(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    store = fields.Nested(ArticleStoreResponse, required=False)
    

