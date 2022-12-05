"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .Trader1 import Trader1

from .ReturnConfig1 import ReturnConfig1







from .InventorySet import InventorySet



from .DimensionResponse import DimensionResponse













from .Quantities import Quantities

from .WeightResponse import WeightResponse





from .BrandMeta import BrandMeta



from .UserSerializer import UserSerializer



from .ManufacturerResponse import ManufacturerResponse

from .CompanyMeta import CompanyMeta







from .PriceMeta import PriceMeta



from .StoreMeta import StoreMeta

from .UserSerializer import UserSerializer




class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    track_inventory = fields.Boolean(required=False)
    
    raw_meta = fields.Dict(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    return_config = fields.Nested(ReturnConfig1, required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    added_on_store = fields.Str(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    stage = fields.Str(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    country_of_origin = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    expiration_date = fields.Str(required=False)
    
    identifier = fields.Dict(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    fragile = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    total_quantity = fields.Int(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    is_set = fields.Boolean(required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    is_active = fields.Boolean(required=False)
    
    size = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    _custom_json = fields.Dict(required=False)
    

