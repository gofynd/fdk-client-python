"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .Trader1 import Trader1











from .UserSerializer import UserSerializer







from .StoreMeta import StoreMeta



from .DimensionResponse import DimensionResponse







from .PriceMeta import PriceMeta

from .WeightResponse import WeightResponse

from .Quantities import Quantities







from .CompanyMeta import CompanyMeta

from .InventorySet import InventorySet

from .BrandMeta import BrandMeta



from .UserSerializer import UserSerializer



from .ManufacturerResponse import ManufacturerResponse








class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    meta = fields.Dict(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    total_quantity = fields.Int(required=False)
    
    raw_meta = fields.Dict(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    country_of_origin = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    size = fields.Str(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    added_on_store = fields.Str(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    is_set = fields.Boolean(required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    stage = fields.Str(required=False)
    
    fragile = fields.Boolean(required=False)
    
    identifier = fields.Dict(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    expiration_date = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    is_active = fields.Boolean(required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    return_config = fields.Dict(required=False)
    
    fynd_meta = fields.Dict(required=False)
    

