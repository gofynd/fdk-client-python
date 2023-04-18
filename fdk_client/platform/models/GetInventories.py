"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .PriceArticle import PriceArticle

from .ManufacturerResponse1 import ManufacturerResponse1













from .UserSerializer import UserSerializer



from .Trader2 import Trader2

from .ReturnConfig2 import ReturnConfig2





from .WeightResponse1 import WeightResponse1

from .UserSerializer import UserSerializer

from .ArticleStoreResponse import ArticleStoreResponse





from .DateMeta import DateMeta



from .CompanyMeta1 import CompanyMeta1



from .DimensionResponse1 import DimensionResponse1





from .BrandMeta1 import BrandMeta1

from .QuantitiesArticle import QuantitiesArticle


class GetInventories(BaseSchema):
    # Catalog swagger.json

    
    tax_identifier = fields.Dict(required=False)
    
    platforms = fields.Dict(required=False)
    
    price = fields.Nested(PriceArticle, required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse1, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    stage = fields.Str(required=False)
    
    trace_id = fields.Str(required=False)
    
    identifier = fields.Dict(required=False)
    
    inventory_updated_on = fields.Str(required=False)
    
    expiration_date = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    trader = fields.List(fields.Nested(Trader2, required=False), required=False)
    
    return_config = fields.Nested(ReturnConfig2, required=False)
    
    uid = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    weight = fields.Nested(WeightResponse1, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    store = fields.Nested(ArticleStoreResponse, required=False)
    
    is_set = fields.Boolean(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    
    total_quantity = fields.Int(required=False)
    
    company = fields.Nested(CompanyMeta1, required=False)
    
    size = fields.Str(required=False)
    
    dimension = fields.Nested(DimensionResponse1, required=False)
    
    id = fields.Str(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    brand = fields.Nested(BrandMeta1, required=False)
    
    quantities = fields.Nested(QuantitiesArticle, required=False)
    
