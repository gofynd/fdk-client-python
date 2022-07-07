"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .UserSerializer import UserSerializer





from .PriceMeta import PriceMeta



from .ManufacturerResponse import ManufacturerResponse

from .Quantities import Quantities

from .UserSerializer import UserSerializer







from .CompanyMeta import CompanyMeta

from .Trader1 import Trader1



from .InventorySet import InventorySet

from .WeightResponse import WeightResponse



from .StoreMeta import StoreMeta





from .BrandMeta import BrandMeta







from .DimensionResponse import DimensionResponse








class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    identifier = fields.Dict(required=False)
    
    is_set = fields.Boolean(required=False)
    
    size = fields.Str(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    raw_meta = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    country_of_origin = fields.Str(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    fragile = fields.Boolean(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    expiration_date = fields.Str(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    return_config = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    added_on_store = fields.Str(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    total_quantity = fields.Int(required=False)
    
    item_id = fields.Int(required=False)
    

