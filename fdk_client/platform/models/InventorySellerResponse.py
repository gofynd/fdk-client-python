"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .DimensionResponse import DimensionResponse

from .WeightResponse import WeightResponse



from .StoreMeta import StoreMeta



from .Quantities import Quantities









from .UserSerializer import UserSerializer













from .CompanyMeta import CompanyMeta



from .UserSerializer import UserSerializer



from .PriceMeta import PriceMeta



from .BrandMeta import BrandMeta







from .Trader1 import Trader1



from .InventorySet import InventorySet

from .ManufacturerResponse import ManufacturerResponse


class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    fynd_meta = fields.Dict(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    added_on_store = fields.Str(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    expiration_date = fields.Str(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    uid = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    return_config = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    raw_meta = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    total_quantity = fields.Int(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    item_id = fields.Int(required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    is_set = fields.Boolean(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    fragile = fields.Boolean(required=False)
    
    identifier = fields.Dict(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    stage = fields.Str(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    

