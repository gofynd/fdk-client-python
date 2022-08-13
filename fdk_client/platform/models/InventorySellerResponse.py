"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .DimensionResponse import DimensionResponse





from .StoreMeta import StoreMeta



















from .CompanyMeta import CompanyMeta



from .InventorySet import InventorySet







from .UserSerializer import UserSerializer





from .Trader1 import Trader1

from .ManufacturerResponse import ManufacturerResponse





from .UserSerializer import UserSerializer

from .PriceMeta import PriceMeta

from .Quantities import Quantities

from .WeightResponse import WeightResponse

from .BrandMeta import BrandMeta




class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    fynd_item_code = fields.Str(required=False)
    
    added_on_store = fields.Str(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    fragile = fields.Boolean(required=False)
    
    total_quantity = fields.Int(required=False)
    
    raw_meta = fields.Dict(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    stage = fields.Str(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    return_config = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    item_id = fields.Int(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    identifier = fields.Dict(required=False)
    
    expiration_date = fields.Str(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    is_set = fields.Boolean(required=False)
    
    size = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    meta = fields.Dict(required=False)
    

