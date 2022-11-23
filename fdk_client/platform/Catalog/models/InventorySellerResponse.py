"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












from .WeightResponse import WeightResponse





from .PriceMeta import PriceMeta





from .InventorySet import InventorySet



from .Trader1 import Trader1







from .DimensionResponse import DimensionResponse





from .BrandMeta import BrandMeta



from .Quantities import Quantities











from .ReturnConfig1 import ReturnConfig1







from .UserSerializer import UserSerializer





from .ManufacturerResponse import ManufacturerResponse



from .UserSerializer import UserSerializer



from .StoreMeta import StoreMeta















from .CompanyMeta import CompanyMeta



class InventorySellerResponse(BaseSchema):
    #  swagger.json

    
    country_of_origin = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    stage = fields.Str(required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    expiration_date = fields.Str(required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    raw_meta = fields.Dict(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    total_quantity = fields.Int(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    item_id = fields.Int(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    added_on_store = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    return_config = fields.Nested(ReturnConfig1, required=False)
    
    fragile = fields.Boolean(required=False)
    
    is_set = fields.Boolean(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    size = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    identifier = fields.Dict(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
