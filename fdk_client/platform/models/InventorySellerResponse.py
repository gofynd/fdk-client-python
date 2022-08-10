"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .BrandMeta import BrandMeta







from .UserSerializer import UserSerializer



from .Trader1 import Trader1

from .PriceMeta import PriceMeta

from .ManufacturerResponse import ManufacturerResponse





from .UserSerializer import UserSerializer



from .InventorySet import InventorySet





from .Quantities import Quantities





from .CompanyMeta import CompanyMeta





from .DimensionResponse import DimensionResponse



from .WeightResponse import WeightResponse









from .StoreMeta import StoreMeta




class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    is_active = fields.Boolean(required=False)
    
    total_quantity = fields.Int(required=False)
    
    is_set = fields.Boolean(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    size = fields.Str(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    item_id = fields.Int(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    meta = fields.Dict(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    expiration_date = fields.Str(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    stage = fields.Str(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    added_on_store = fields.Str(required=False)
    
    fragile = fields.Boolean(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    return_config = fields.Dict(required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    identifier = fields.Dict(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    raw_meta = fields.Dict(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    country_of_origin = fields.Str(required=False)
    

