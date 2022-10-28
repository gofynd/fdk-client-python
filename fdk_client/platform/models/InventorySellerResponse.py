"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CompanyMeta import CompanyMeta



from .UserSerializer import UserSerializer





from .StoreMeta import StoreMeta





from .InventorySet import InventorySet

from .WeightResponse import WeightResponse

from .ManufacturerResponse import ManufacturerResponse

from .DimensionResponse import DimensionResponse

from .Quantities import Quantities





from .UserSerializer import UserSerializer

from .ReturnConfig1 import ReturnConfig1







from .BrandMeta import BrandMeta



from .PriceMeta import PriceMeta





from .Trader1 import Trader1




















class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    company = fields.Nested(CompanyMeta, required=False)
    
    expiration_date = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    fragile = fields.Boolean(required=False)
    
    is_set = fields.Boolean(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    total_quantity = fields.Int(required=False)
    
    raw_meta = fields.Dict(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    return_config = fields.Nested(ReturnConfig1, required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    added_on_store = fields.Str(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    identifier = fields.Dict(required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    stage = fields.Str(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    item_id = fields.Int(required=False)
    
    uid = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    size = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    tax_identifier = fields.Dict(required=False)
    

