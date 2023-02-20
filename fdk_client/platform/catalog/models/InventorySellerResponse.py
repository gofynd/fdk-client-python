"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .PriceMeta import PriceMeta



from .InventorySet import InventorySet





from .UserSerializer import UserSerializer







from .UserSerializer import UserSerializer



from .BrandMeta import BrandMeta





from .WeightResponse import WeightResponse

















from .ReturnConfig2 import ReturnConfig2









from .Quantities import Quantities



from .ManufacturerResponse import ManufacturerResponse





from .CompanyMeta import CompanyMeta



from .Trader2 import Trader2









from .StoreMeta import StoreMeta





from .DimensionResponse import DimensionResponse











class InventorySellerResponse(BaseSchema):
    #  swagger.json

    
    price = fields.Nested(PriceMeta, required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    country_of_origin = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    expiration_date = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    is_active = fields.Boolean(required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    raw_meta = fields.Dict(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    stage = fields.Str(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    return_config = fields.Nested(ReturnConfig2, required=False)
    
    identifier = fields.Dict(required=False)
    
    fragile = fields.Boolean(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    total_quantity = fields.Int(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    trader = fields.List(fields.Nested(Trader2, required=False), required=False)
    
    added_on_store = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    is_set = fields.Boolean(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    trace_id = fields.Str(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    item_id = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    
