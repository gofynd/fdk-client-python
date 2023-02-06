"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .WeightResponse import WeightResponse





from .UserSerializer import UserSerializer



from .ReturnConfig2 import ReturnConfig2



















from .DimensionResponse import DimensionResponse





from .UserSerializer import UserSerializer









from .ManufacturerResponse import ManufacturerResponse





from .BrandMeta import BrandMeta



from .StoreMeta import StoreMeta





from .CompanyMeta import CompanyMeta



from .PriceMeta import PriceMeta











from .InventorySet import InventorySet



from .Quantities import Quantities





from .Trader2 import Trader2





class InventorySellerResponse(BaseSchema):
    #  swagger.json

    
    is_active = fields.Boolean(required=False)
    
    stage = fields.Str(required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    country_of_origin = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    return_config = fields.Nested(ReturnConfig2, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    fragile = fields.Boolean(required=False)
    
    size = fields.Str(required=False)
    
    trace_id = fields.Str(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    expiration_date = fields.Str(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    uid = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    raw_meta = fields.Dict(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    identifier = fields.Dict(required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    item_id = fields.Int(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    added_on_store = fields.Str(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    total_quantity = fields.Int(required=False)
    
    trader = fields.List(fields.Nested(Trader2, required=False), required=False)
    
    tax_identifier = fields.Dict(required=False)
    
