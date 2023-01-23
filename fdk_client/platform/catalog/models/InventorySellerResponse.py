"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .PriceMeta import PriceMeta



from .UserSerializer import UserSerializer











from .ReturnConfig2 import ReturnConfig2



from .ManufacturerResponse import ManufacturerResponse



from .DimensionResponse import DimensionResponse







from .InventorySet import InventorySet











from .CompanyMeta import CompanyMeta







from .BrandMeta import BrandMeta







from .Quantities import Quantities



from .StoreMeta import StoreMeta



from .Trader2 import Trader2





from .UserSerializer import UserSerializer















from .WeightResponse import WeightResponse





class InventorySellerResponse(BaseSchema):
    #  swagger.json

    
    seller_identifier = fields.Str(required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    uid = fields.Str(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    expiration_date = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    return_config = fields.Nested(ReturnConfig2, required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    fragile = fields.Boolean(required=False)
    
    identifier = fields.Dict(required=False)
    
    added_on_store = fields.Str(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    size = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    raw_meta = fields.Dict(required=False)
    
    trace_id = fields.Str(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    trader = fields.List(fields.Nested(Trader2, required=False), required=False)
    
    item_id = fields.Int(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    meta = fields.Dict(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    stage = fields.Str(required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    total_quantity = fields.Int(required=False)
    
