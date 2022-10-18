"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .StoreMeta import StoreMeta





from .WeightResponse import WeightResponse





from .Trader1 import Trader1



from .CompanyMeta import CompanyMeta











from .DimensionResponse import DimensionResponse

from .UserSerializer import UserSerializer









from .ManufacturerResponse import ManufacturerResponse

from .UserSerializer import UserSerializer

from .InventorySet import InventorySet



from .BrandMeta import BrandMeta







from .Quantities import Quantities





from .ReturnConfig1 import ReturnConfig1

from .PriceMeta import PriceMeta


class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    fynd_item_code = fields.Str(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    is_set = fields.Boolean(required=False)
    
    added_on_store = fields.Str(required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    total_quantity = fields.Int(required=False)
    
    uid = fields.Str(required=False)
    
    fragile = fields.Boolean(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    stage = fields.Str(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    size = fields.Str(required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    identifier = fields.Dict(required=False)
    
    raw_meta = fields.Dict(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    expiration_date = fields.Str(required=False)
    
    return_config = fields.Nested(ReturnConfig1, required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    

