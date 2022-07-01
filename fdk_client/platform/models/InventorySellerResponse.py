"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Dimension import Dimension

from .UserSerializer import UserSerializer













from .UserSerializer import UserSerializer

from .Weight import Weight





from .BrandMeta import BrandMeta

from .StoreMeta import StoreMeta







from .InventorySet import InventorySet

from .Trader1 import Trader1









from .Manufacturer import Manufacturer





from .CompanyMeta import CompanyMeta

from .Quantities import Quantities









from .PriceMeta import PriceMeta


class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    dimension = fields.Nested(Dimension, required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    country_of_origin = fields.Str(required=False)
    
    raw_meta = fields.Dict(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    item_id = fields.Int(required=False)
    
    is_set = fields.Boolean(required=False)
    
    total_quantity = fields.Int(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    weight = fields.Nested(Weight, required=False)
    
    size = fields.Str(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    added_on_store = fields.Str(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    fragile = fields.Boolean(required=False)
    
    identifier = fields.Dict(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    manufacturer = fields.Nested(Manufacturer, required=False)
    
    expiration_date = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    return_config = fields.Dict(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    

