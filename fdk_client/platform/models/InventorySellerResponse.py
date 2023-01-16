"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .WeightResponse import WeightResponse

from .UserSerializer import UserSerializer

from .StoreMeta import StoreMeta



from .BrandMeta import BrandMeta







from .Quantities import Quantities

from .PriceMeta import PriceMeta













from .CompanyMeta import CompanyMeta







from .ManufacturerResponse import ManufacturerResponse



from .ReturnConfig1 import ReturnConfig1

from .InventorySet import InventorySet









from .Trader1 import Trader1

from .UserSerializer import UserSerializer











from .DimensionResponse import DimensionResponse


class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    weight = fields.Nested(WeightResponse, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    is_active = fields.Boolean(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    identifier = fields.Dict(required=False)
    
    raw_meta = fields.Dict(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    item_id = fields.Int(required=False)
    
    fragile = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    size = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    is_set = fields.Boolean(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    added_on_store = fields.Str(required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    expiration_date = fields.Str(required=False)
    
    return_config = fields.Nested(ReturnConfig1, required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    total_quantity = fields.Int(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    trace_id = fields.Str(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    

