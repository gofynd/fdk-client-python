"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .CompanyMeta import CompanyMeta





from .Quantities import Quantities



from .InventorySet import InventorySet

from .ManufacturerResponse import ManufacturerResponse

from .BrandMeta import BrandMeta























from .ReturnConfig1 import ReturnConfig1

from .Trader1 import Trader1

from .DimensionResponse import DimensionResponse







from .WeightResponse import WeightResponse

from .UserSerializer import UserSerializer

from .StoreMeta import StoreMeta



from .UserSerializer import UserSerializer



from .PriceMeta import PriceMeta




class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    seller_identifier = fields.Str(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    is_active = fields.Boolean(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    country_of_origin = fields.Str(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    raw_meta = fields.Dict(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    fragile = fields.Boolean(required=False)
    
    expiration_date = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    
    identifier = fields.Dict(required=False)
    
    total_quantity = fields.Int(required=False)
    
    is_set = fields.Boolean(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    return_config = fields.Nested(ReturnConfig1, required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    added_on_store = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    size = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    track_inventory = fields.Boolean(required=False)
    

