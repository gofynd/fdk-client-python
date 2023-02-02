"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .Quantities import Quantities





from .ManufacturerResponse import ManufacturerResponse









from .Trader2 import Trader2









from .UserSerializer import UserSerializer





from .ReturnConfig2 import ReturnConfig2



from .WeightResponse import WeightResponse









from .DimensionResponse import DimensionResponse



from .CompanyMeta import CompanyMeta





from .BrandMeta import BrandMeta



from .PriceMeta import PriceMeta





from .StoreMeta import StoreMeta











from .InventorySet import InventorySet









from .UserSerializer import UserSerializer



class InventorySellerResponse(BaseSchema):
    #  swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    total_quantity = fields.Int(required=False)
    
    meta = fields.Dict(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    uid = fields.Str(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    trader = fields.List(fields.Nested(Trader2, required=False), required=False)
    
    trace_id = fields.Str(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    item_id = fields.Int(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    is_set = fields.Boolean(required=False)
    
    return_config = fields.Nested(ReturnConfig2, required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    added_on_store = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    stage = fields.Str(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    size = fields.Str(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    identifier = fields.Dict(required=False)
    
    expiration_date = fields.Str(required=False)
    
    raw_meta = fields.Dict(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    fragile = fields.Boolean(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
