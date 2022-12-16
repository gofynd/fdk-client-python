"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .BrandMeta import BrandMeta











from .CompanyMeta import CompanyMeta



from .Trader1 import Trader1







from .InventorySet import InventorySet









from .WeightResponse import WeightResponse





from .UserSerializer import UserSerializer





from .PriceMeta import PriceMeta



from .UserSerializer import UserSerializer



from .StoreMeta import StoreMeta















from .Quantities import Quantities



from .ReturnConfig1 import ReturnConfig1



from .DimensionResponse import DimensionResponse



from .ManufacturerResponse import ManufacturerResponse















class InventorySellerResponse(BaseSchema):
    #  swagger.json

    
    brand = fields.Nested(BrandMeta, required=False)
    
    total_quantity = fields.Int(required=False)
    
    expiration_date = fields.Str(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    item_id = fields.Int(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    country_of_origin = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    identifier = fields.Dict(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    meta = fields.Dict(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    added_on_store = fields.Str(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    stage = fields.Str(required=False)
    
    trace_id = fields.Str(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    return_config = fields.Nested(ReturnConfig1, required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    raw_meta = fields.Dict(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    fragile = fields.Boolean(required=False)
    
    is_set = fields.Boolean(required=False)
    
    fynd_item_code = fields.Str(required=False)
    