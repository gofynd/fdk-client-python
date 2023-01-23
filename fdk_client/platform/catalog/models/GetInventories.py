"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .DimensionResponse import DimensionResponse





from .Trader2 import Trader2



from .UserSerializer import UserSerializer





from .BrandMeta import BrandMeta







from .UserSerializer import UserSerializer





from .InventorySet import InventorySet







from .ReturnConfig2 import ReturnConfig2







from .ManufacturerResponse import ManufacturerResponse





from .CompanyMeta import CompanyMeta























from .WeightResponse import WeightResponse







from .ArticleStoreResponse import ArticleStoreResponse





from .PriceMeta import PriceMeta





class GetInventories(BaseSchema):
    #  swagger.json

    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    trace_id = fields.Str(required=False)
    
    trader = fields.List(fields.Nested(Trader2, required=False), required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    total_quantity = fields.Int(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    fragile = fields.Boolean(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    item_id = fields.Int(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    meta = fields.Dict(required=False)
    
    inventory_updated_on = fields.Str(required=False)
    
    return_config = fields.Nested(ReturnConfig2, required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    raw_meta = fields.Dict(required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    country_of_origin = fields.Str(required=False)
    
    identifier = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    added_on_store = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    expiration_date = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    store = fields.Nested(ArticleStoreResponse, required=False)
    
    size = fields.Str(required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
