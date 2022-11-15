"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Trader1 import Trader1



from .InventorySet import InventorySet































from .UserSerializer import UserSerializer



from .ReturnConfig1 import ReturnConfig1



from .UserSerializer import UserSerializer



from .ManufacturerResponse import ManufacturerResponse







from .Quantities import Quantities







from .WeightResponse import WeightResponse



from .DimensionResponse import DimensionResponse





from .StoreMeta import StoreMeta











from .CompanyMeta import CompanyMeta



from .PriceMeta import PriceMeta



from .BrandMeta import BrandMeta



class InventorySellerResponse(BaseSchema):
    #  swagger.json

    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    total_quantity = fields.Int(required=False)
    
    is_set = fields.Boolean(required=False)
    
    fragile = fields.Boolean(required=False)
    
    stage = fields.Str(required=False)
    
    expiration_date = fields.Str(required=False)
    
    identifier = fields.Dict(required=False)
    
    item_id = fields.Int(required=False)
    
    added_on_store = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    return_config = fields.Nested(ReturnConfig1, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    trace_id = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    raw_meta = fields.Dict(required=False)
    
    size = fields.Str(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
