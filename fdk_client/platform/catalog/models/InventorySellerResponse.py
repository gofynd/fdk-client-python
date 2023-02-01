"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .CompanyMeta import CompanyMeta









from .StoreMeta import StoreMeta





from .UserSerializer import UserSerializer



from .PriceMeta import PriceMeta





from .Quantities import Quantities



from .DimensionResponse import DimensionResponse











from .ManufacturerResponse import ManufacturerResponse





from .UserSerializer import UserSerializer



from .BrandMeta import BrandMeta



from .ReturnConfig2 import ReturnConfig2





from .Trader2 import Trader2













from .InventorySet import InventorySet







from .WeightResponse import WeightResponse











class InventorySellerResponse(BaseSchema):
    #  swagger.json

    
    track_inventory = fields.Boolean(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    trace_id = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    expiration_date = fields.Str(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    raw_meta = fields.Dict(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    identifier = fields.Dict(required=False)
    
    stage = fields.Str(required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    is_active = fields.Boolean(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    return_config = fields.Nested(ReturnConfig2, required=False)
    
    meta = fields.Dict(required=False)
    
    trader = fields.List(fields.Nested(Trader2, required=False), required=False)
    
    country_of_origin = fields.Str(required=False)
    
    total_quantity = fields.Int(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    item_id = fields.Int(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    size = fields.Str(required=False)
    
    fragile = fields.Boolean(required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    is_set = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    added_on_store = fields.Str(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
