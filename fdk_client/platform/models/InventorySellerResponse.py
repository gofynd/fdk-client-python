"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema













from .StoreMeta import StoreMeta











from .PriceMeta import PriceMeta



from .InventorySet import InventorySet

from .ManufacturerResponse import ManufacturerResponse









from .BrandMeta import BrandMeta







from .WeightResponse import WeightResponse

from .Quantities import Quantities

from .CompanyMeta import CompanyMeta





from .DimensionResponse import DimensionResponse



from .ReturnConfig1 import ReturnConfig1

from .Trader1 import Trader1

from .UserSerializer import UserSerializer

from .UserSerializer import UserSerializer




class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    trace_id = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    added_on_store = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    expiration_date = fields.Str(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    fragile = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_set = fields.Boolean(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    identifier = fields.Dict(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    total_quantity = fields.Int(required=False)
    
    uid = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    item_id = fields.Int(required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    raw_meta = fields.Dict(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    size = fields.Str(required=False)
    
    return_config = fields.Nested(ReturnConfig1, required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    tax_identifier = fields.Dict(required=False)
    

