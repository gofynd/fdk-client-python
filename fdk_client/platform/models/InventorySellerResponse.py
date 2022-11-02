"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .UserSerializer import UserSerializer



from .ReturnConfig1 import ReturnConfig1



from .ManufacturerResponse import ManufacturerResponse

from .StoreMeta import StoreMeta

from .Trader1 import Trader1

from .CompanyMeta import CompanyMeta





from .Quantities import Quantities

from .UserSerializer import UserSerializer











from .WeightResponse import WeightResponse



from .DimensionResponse import DimensionResponse



from .PriceMeta import PriceMeta









from .BrandMeta import BrandMeta



from .InventorySet import InventorySet


class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    item_id = fields.Int(required=False)
    
    uid = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    fragile = fields.Boolean(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    raw_meta = fields.Dict(required=False)
    
    return_config = fields.Nested(ReturnConfig1, required=False)
    
    is_set = fields.Boolean(required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    meta = fields.Dict(required=False)
    
    expiration_date = fields.Str(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    stage = fields.Str(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    size = fields.Str(required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    total_quantity = fields.Int(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    identifier = fields.Dict(required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    country_of_origin = fields.Str(required=False)
    
    added_on_store = fields.Str(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    

