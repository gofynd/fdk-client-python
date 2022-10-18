"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .InventorySet import InventorySet







from .UserSerializer import UserSerializer







from .StoreMeta import StoreMeta

from .ReturnConfig1 import ReturnConfig1



from .Trader1 import Trader1















from .Quantities import Quantities

from .BrandMeta import BrandMeta





from .PriceMeta import PriceMeta





from .UserSerializer import UserSerializer



from .WeightResponse import WeightResponse



from .CompanyMeta import CompanyMeta

from .DimensionResponse import DimensionResponse

from .ManufacturerResponse import ManufacturerResponse




class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    total_quantity = fields.Int(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    added_on_store = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    return_config = fields.Nested(ReturnConfig1, required=False)
    
    fragile = fields.Boolean(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    item_id = fields.Int(required=False)
    
    stage = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    identifier = fields.Dict(required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    expiration_date = fields.Str(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    raw_meta = fields.Dict(required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    is_set = fields.Boolean(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    size = fields.Str(required=False)
    

