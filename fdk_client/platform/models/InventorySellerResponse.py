"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .CompanyMeta import CompanyMeta





from .Trader1 import Trader1





from .PriceMeta import PriceMeta

from .WeightResponse import WeightResponse





from .DimensionResponse import DimensionResponse







from .UserSerializer import UserSerializer





from .InventorySet import InventorySet





from .UserSerializer import UserSerializer



from .BrandMeta import BrandMeta





from .StoreMeta import StoreMeta

from .ReturnConfig1 import ReturnConfig1



from .ManufacturerResponse import ManufacturerResponse



from .Quantities import Quantities




class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    track_inventory = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    identifier = fields.Dict(required=False)
    
    fragile = fields.Boolean(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    raw_meta = fields.Dict(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    is_set = fields.Boolean(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    total_quantity = fields.Int(required=False)
    
    added_on_store = fields.Str(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    expiration_date = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    item_id = fields.Int(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    return_config = fields.Nested(ReturnConfig1, required=False)
    
    country_of_origin = fields.Str(required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    stage = fields.Str(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    size = fields.Str(required=False)
    

