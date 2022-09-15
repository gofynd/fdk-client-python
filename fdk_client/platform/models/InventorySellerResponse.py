"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .CompanyMeta import CompanyMeta



from .StoreMeta import StoreMeta

from .BrandMeta import BrandMeta

from .InventorySet import InventorySet

from .UserSerializer import UserSerializer



from .Quantities import Quantities



from .ReturnConfig1 import ReturnConfig1



from .Trader1 import Trader1

from .WeightResponse import WeightResponse















from .DimensionResponse import DimensionResponse

from .UserSerializer import UserSerializer





from .ManufacturerResponse import ManufacturerResponse



from .PriceMeta import PriceMeta








class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    country_of_origin = fields.Str(required=False)
    
    added_on_store = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    size = fields.Str(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    raw_meta = fields.Dict(required=False)
    
    return_config = fields.Nested(ReturnConfig1, required=False)
    
    uid = fields.Str(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    meta = fields.Dict(required=False)
    
    expiration_date = fields.Str(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    fragile = fields.Boolean(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    identifier = fields.Dict(required=False)
    
    total_quantity = fields.Int(required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    is_active = fields.Boolean(required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    is_set = fields.Boolean(required=False)
    

