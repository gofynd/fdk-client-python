"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .Quantities import Quantities

from .BrandMeta import BrandMeta













from .Trader1 import Trader1

from .ManufacturerResponse import ManufacturerResponse

from .CompanyMeta import CompanyMeta

from .UserSerializer import UserSerializer









from .WeightResponse import WeightResponse

from .DimensionResponse import DimensionResponse

from .StoreMeta import StoreMeta













from .ReturnConfig1 import ReturnConfig1











from .UserSerializer import UserSerializer

from .PriceMeta import PriceMeta

from .InventorySet import InventorySet


class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    added_on_store = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    item_id = fields.Int(required=False)
    
    identifier = fields.Dict(required=False)
    
    expiration_date = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    total_quantity = fields.Int(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    net_quantity_unit = fields.Raw(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    fragile = fields.Boolean(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    meta = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    net_quantity_value = fields.Float(required=False)
    
    size = fields.Str(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    stage = fields.Str(required=False)
    
    return_config = fields.Nested(ReturnConfig1, required=False)
    
    raw_meta = fields.Dict(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    set = fields.Nested(InventorySet, required=False)
    

