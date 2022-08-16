"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Trader1 import Trader1





from .Quantities import Quantities

from .InventorySet import InventorySet











from .ReturnConfig1 import ReturnConfig1

from .StoreMeta import StoreMeta







from .DimensionResponse import DimensionResponse

from .ManufacturerResponse import ManufacturerResponse



from .UserSerializer import UserSerializer

from .PriceMeta import PriceMeta

from .UserSerializer import UserSerializer









from .CompanyMeta import CompanyMeta





from .BrandMeta import BrandMeta





from .WeightResponse import WeightResponse






class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    stage = fields.Str(required=False)
    
    raw_meta = fields.Dict(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    total_quantity = fields.Int(required=False)
    
    return_config = fields.Nested(ReturnConfig1, required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    identifier = fields.Dict(required=False)
    
    fragile = fields.Boolean(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    is_active = fields.Boolean(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    country_of_origin = fields.Str(required=False)
    
    expiration_date = fields.Str(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    is_set = fields.Boolean(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    added_on_store = fields.Str(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    item_id = fields.Int(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    size = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    

