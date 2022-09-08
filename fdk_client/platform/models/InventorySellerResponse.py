"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .UserSerializer import UserSerializer















from .CompanyMeta import CompanyMeta





from .Trader1 import Trader1









from .Quantities import Quantities





from .ReturnConfig1 import ReturnConfig1

from .WeightResponse import WeightResponse

from .PriceMeta import PriceMeta

from .UserSerializer import UserSerializer

from .InventorySet import InventorySet

from .DimensionResponse import DimensionResponse

from .StoreMeta import StoreMeta



from .BrandMeta import BrandMeta





from .ManufacturerResponse import ManufacturerResponse


class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    identifier = fields.Dict(required=False)
    
    item_id = fields.Int(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    uid = fields.Str(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    stage = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    size = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    raw_meta = fields.Dict(required=False)
    
    fragile = fields.Boolean(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    expiration_date = fields.Str(required=False)
    
    added_on_store = fields.Str(required=False)
    
    return_config = fields.Nested(ReturnConfig1, required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    total_quantity = fields.Int(required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    

