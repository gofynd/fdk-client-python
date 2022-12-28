"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Quantities import Quantities







from .PriceMeta import PriceMeta

from .DimensionResponse import DimensionResponse







from .UserSerializer import UserSerializer

from .BrandMeta import BrandMeta





from .CompanyMeta import CompanyMeta











from .InventorySet import InventorySet







from .ManufacturerResponse import ManufacturerResponse





from .StoreMeta import StoreMeta

from .ReturnConfig1 import ReturnConfig1

from .Trader1 import Trader1









from .WeightResponse import WeightResponse

from .UserSerializer import UserSerializer




class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    quantities = fields.Nested(Quantities, required=False)
    
    meta = fields.Dict(required=False)
    
    stage = fields.Str(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    fragile = fields.Boolean(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    expiration_date = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    uid = fields.Str(required=False)
    
    identifier = fields.Dict(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    is_set = fields.Boolean(required=False)
    
    trace_id = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    country_of_origin = fields.Str(required=False)
    
    raw_meta = fields.Dict(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    return_config = fields.Nested(ReturnConfig1, required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    total_quantity = fields.Int(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    item_id = fields.Int(required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    added_on_store = fields.Str(required=False)
    

