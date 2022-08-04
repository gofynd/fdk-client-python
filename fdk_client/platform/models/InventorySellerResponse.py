"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .StoreMeta import StoreMeta

from .UserSerializer import UserSerializer





from .DimensionResponse import DimensionResponse

from .WeightResponse import WeightResponse

from .PriceMeta import PriceMeta





from .Quantities import Quantities









from .InventorySet import InventorySet

from .UserSerializer import UserSerializer



from .BrandMeta import BrandMeta





from .ManufacturerResponse import ManufacturerResponse







from .Trader1 import Trader1









from .CompanyMeta import CompanyMeta


class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    is_active = fields.Boolean(required=False)
    
    item_id = fields.Int(required=False)
    
    expiration_date = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    country_of_origin = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    fragile = fields.Boolean(required=False)
    
    raw_meta = fields.Dict(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    total_quantity = fields.Int(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    added_on_store = fields.Str(required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    uid = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    return_config = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    identifier = fields.Dict(required=False)
    
    is_set = fields.Boolean(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    

