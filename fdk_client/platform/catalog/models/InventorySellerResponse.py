"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




















from .DimensionResponse import DimensionResponse







from .UserSerializer import UserSerializer



from .Quantities import Quantities



from .ManufacturerResponse import ManufacturerResponse











from .UserSerializer import UserSerializer



from .StoreMeta import StoreMeta





from .ReturnConfig2 import ReturnConfig2



from .PriceMeta import PriceMeta



from .Trader2 import Trader2





from .WeightResponse import WeightResponse





from .InventorySet import InventorySet





from .CompanyMeta import CompanyMeta













from .BrandMeta import BrandMeta



class InventorySellerResponse(BaseSchema):
    #  swagger.json

    
    raw_meta = fields.Dict(required=False)
    
    item_id = fields.Int(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    added_on_store = fields.Str(required=False)
    
    total_quantity = fields.Int(required=False)
    
    identifier = fields.Dict(required=False)
    
    fragile = fields.Boolean(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    stage = fields.Str(required=False)
    
    expiration_date = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    country_of_origin = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    is_active = fields.Boolean(required=False)
    
    return_config = fields.Nested(ReturnConfig2, required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    trader = fields.List(fields.Nested(Trader2, required=False), required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    size = fields.Str(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    trace_id = fields.Str(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
