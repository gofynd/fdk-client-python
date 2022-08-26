"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PriceMeta import PriceMeta







from .ReturnConfig1 import ReturnConfig1

from .BrandMeta import BrandMeta







from .ManufacturerResponse import ManufacturerResponse

from .StoreMeta import StoreMeta











from .Trader1 import Trader1



from .DimensionResponse import DimensionResponse









from .CompanyMeta import CompanyMeta







from .WeightResponse import WeightResponse

from .UserSerializer import UserSerializer



from .UserSerializer import UserSerializer

from .Quantities import Quantities

from .InventorySet import InventorySet




class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    price = fields.Nested(PriceMeta, required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    return_config = fields.Nested(ReturnConfig1, required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    expiration_date = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    uid = fields.Str(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    stage = fields.Str(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    identifier = fields.Dict(required=False)
    
    total_quantity = fields.Int(required=False)
    
    fragile = fields.Boolean(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    item_id = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    added_on_store = fields.Str(required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    country_of_origin = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    raw_meta = fields.Dict(required=False)
    

