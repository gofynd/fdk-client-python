"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .CompanyMeta import CompanyMeta











from .UserSerializer import UserSerializer





from .BrandMeta import BrandMeta



from .DimensionResponse import DimensionResponse



from .Quantities import Quantities











from .StoreMeta import StoreMeta



from .InventorySet import InventorySet







from .WeightResponse import WeightResponse



from .UserSerializer import UserSerializer



from .Trader2 import Trader2



from .PriceMeta import PriceMeta























from .ReturnConfig2 import ReturnConfig2



from .ManufacturerResponse import ManufacturerResponse



class InventorySellerResponse(BaseSchema):
    #  swagger.json

    
    fynd_article_code = fields.Str(required=False)
    
    trace_id = fields.Str(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    stage = fields.Str(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    fragile = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    item_id = fields.Int(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    raw_meta = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    
    total_quantity = fields.Int(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    expiration_date = fields.Str(required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    trader = fields.List(fields.Nested(Trader2, required=False), required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    added_on_store = fields.Str(required=False)
    
    identifier = fields.Dict(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    size = fields.Str(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    is_set = fields.Boolean(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    return_config = fields.Nested(ReturnConfig2, required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
