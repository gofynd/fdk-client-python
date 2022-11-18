"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ReturnConfig1 import ReturnConfig1







from .InventorySet import InventorySet





from .DimensionResponse import DimensionResponse

from .Quantities import Quantities



from .WeightResponse import WeightResponse



from .StoreMeta import StoreMeta

from .CompanyMeta import CompanyMeta

from .ManufacturerResponse import ManufacturerResponse





from .PriceMeta import PriceMeta

from .BrandMeta import BrandMeta











from .UserSerializer import UserSerializer



from .UserSerializer import UserSerializer







from .Trader1 import Trader1










class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    return_config = fields.Nested(ReturnConfig1, required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    stage = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    meta = fields.Dict(required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    item_id = fields.Int(required=False)
    
    raw_meta = fields.Dict(required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    is_set = fields.Boolean(required=False)
    
    uid = fields.Str(required=False)
    
    fragile = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    identifier = fields.Dict(required=False)
    
    expiration_date = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    total_quantity = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    added_on_store = fields.Str(required=False)
    
    track_inventory = fields.Boolean(required=False)
    

