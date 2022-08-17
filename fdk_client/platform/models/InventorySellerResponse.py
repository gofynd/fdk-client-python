"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .InventorySet import InventorySet









from .StoreMeta import StoreMeta







from .Trader1 import Trader1





from .ManufacturerResponse import ManufacturerResponse











from .UserSerializer import UserSerializer





from .WeightResponse import WeightResponse





from .Quantities import Quantities



from .ReturnConfig1 import ReturnConfig1

from .CompanyMeta import CompanyMeta

from .BrandMeta import BrandMeta

from .UserSerializer import UserSerializer



from .DimensionResponse import DimensionResponse

from .PriceMeta import PriceMeta




class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    set = fields.Nested(InventorySet, required=False)
    
    is_active = fields.Boolean(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    identifier = fields.Dict(required=False)
    
    item_id = fields.Int(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    total_quantity = fields.Int(required=False)
    
    meta = fields.Dict(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    raw_meta = fields.Dict(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    expiration_date = fields.Str(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    fragile = fields.Boolean(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    added_on_store = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    is_set = fields.Boolean(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    size = fields.Str(required=False)
    
    return_config = fields.Nested(ReturnConfig1, required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    stage = fields.Str(required=False)
    

