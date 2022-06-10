"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .StoreMeta import StoreMeta



from .UserSerializer import UserSerializer



from .Trader1 import Trader1



from .Dimension import Dimension





from .Quantities import Quantities









from .Weight import Weight





from .PriceMeta import PriceMeta

from .Manufacturer import Manufacturer

from .CompanyMeta import CompanyMeta

from .UserSerializer import UserSerializer



from .BrandMeta import BrandMeta















from .InventorySet import InventorySet


class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    item_id = fields.Int(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    identifier = fields.Dict(required=False)
    
    dimension = fields.Nested(Dimension, required=False)
    
    size = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    meta = fields.Dict(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    fragile = fields.Boolean(required=False)
    
    expiration_date = fields.Str(required=False)
    
    weight = fields.Nested(Weight, required=False)
    
    total_quantity = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    manufacturer = fields.Nested(Manufacturer, required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    raw_meta = fields.Dict(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    uid = fields.Str(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    return_config = fields.Dict(required=False)
    
    added_on_store = fields.Str(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    

