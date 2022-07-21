"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .InventorySet import InventorySet





from .StoreMeta import StoreMeta



from .BrandMeta import BrandMeta

from .CompanyMeta import CompanyMeta









from .UserSerializer import UserSerializer











from .Quantities import Quantities

from .ManufacturerResponse import ManufacturerResponse



from .PriceMeta import PriceMeta











from .Trader1 import Trader1



from .UserSerializer import UserSerializer



from .WeightResponse import WeightResponse

from .DimensionResponse import DimensionResponse






class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    set = fields.Nested(InventorySet, required=False)
    
    return_config = fields.Dict(required=False)
    
    total_quantity = fields.Int(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    added_on_store = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    expiration_date = fields.Str(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    size = fields.Str(required=False)
    
    fragile = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    country_of_origin = fields.Str(required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    uid = fields.Str(required=False)
    
    raw_meta = fields.Dict(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    identifier = fields.Dict(required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    

