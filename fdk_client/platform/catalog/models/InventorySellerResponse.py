"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .Trader2 import Trader2



from .CompanyMeta import CompanyMeta













from .UserSerializer import UserSerializer



from .Quantities import Quantities



from .StoreMeta import StoreMeta



from .ManufacturerResponse import ManufacturerResponse





from .BrandMeta import BrandMeta

















from .InventorySet import InventorySet



from .UserSerializer import UserSerializer







from .WeightResponse import WeightResponse









from .ReturnConfig2 import ReturnConfig2







from .DimensionResponse import DimensionResponse



from .PriceMeta import PriceMeta







class InventorySellerResponse(BaseSchema):
    #  swagger.json

    
    fragile = fields.Boolean(required=False)
    
    trader = fields.List(fields.Nested(Trader2, required=False), required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    item_id = fields.Int(required=False)
    
    meta = fields.Dict(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    added_on_store = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    is_set = fields.Boolean(required=False)
    
    expiration_date = fields.Str(required=False)
    
    trace_id = fields.Str(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    total_quantity = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    identifier = fields.Dict(required=False)
    
    raw_meta = fields.Dict(required=False)
    
    return_config = fields.Nested(ReturnConfig2, required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    stage = fields.Str(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    country_of_origin = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
