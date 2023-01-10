"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .StoreMeta import StoreMeta





from .UserSerializer import UserSerializer





from .UserSerializer import UserSerializer



from .InventorySet import InventorySet



from .BrandMeta import BrandMeta



from .CompanyMeta import CompanyMeta







from .DimensionResponse import DimensionResponse









from .Quantities import Quantities













from .ManufacturerResponse import ManufacturerResponse





from .Trader2 import Trader2



from .WeightResponse import WeightResponse







from .ReturnConfig2 import ReturnConfig2











from .PriceMeta import PriceMeta









class InventorySellerResponse(BaseSchema):
    #  swagger.json

    
    trace_id = fields.Str(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    is_set = fields.Boolean(required=False)
    
    item_id = fields.Int(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    fragile = fields.Boolean(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    added_on_store = fields.Str(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    stage = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    raw_meta = fields.Dict(required=False)
    
    expiration_date = fields.Str(required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    uid = fields.Str(required=False)
    
    trader = fields.List(fields.Nested(Trader2, required=False), required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    meta = fields.Dict(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    return_config = fields.Nested(ReturnConfig2, required=False)
    
    identifier = fields.Dict(required=False)
    
    total_quantity = fields.Int(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
