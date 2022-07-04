"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Quantities import Quantities

from .PriceMeta import PriceMeta

from .UserSerializer import UserSerializer















from .UserSerializer import UserSerializer





from .BrandMeta import BrandMeta

from .Weight import Weight





from .StoreMeta import StoreMeta





from .CompanyMeta import CompanyMeta





from .Trader1 import Trader1

from .Manufacturer import Manufacturer

from .InventorySet import InventorySet







from .Dimension import Dimension








class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    quantities = fields.Nested(Quantities, required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    return_config = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    expiration_date = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    added_on_store = fields.Str(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    weight = fields.Nested(Weight, required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_set = fields.Boolean(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    size = fields.Str(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    raw_meta = fields.Dict(required=False)
    
    item_id = fields.Int(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    manufacturer = fields.Nested(Manufacturer, required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    identifier = fields.Dict(required=False)
    
    fragile = fields.Boolean(required=False)
    
    dimension = fields.Nested(Dimension, required=False)
    
    total_quantity = fields.Int(required=False)
    
    meta = fields.Dict(required=False)
    
    fynd_meta = fields.Dict(required=False)
    

