"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .Weight import Weight



from .UserSerializer import UserSerializer



from .UserSerializer import UserSerializer

from .Manufacturer import Manufacturer

from .Quantities import Quantities



from .Trader1 import Trader1

from .InventorySet import InventorySet













from .StoreMeta import StoreMeta

from .BrandMeta import BrandMeta











from .PriceMeta import PriceMeta

from .Dimension import Dimension

from .CompanyMeta import CompanyMeta






class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    raw_meta = fields.Dict(required=False)
    
    expiration_date = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    weight = fields.Nested(Weight, required=False)
    
    return_config = fields.Dict(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    size = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    manufacturer = fields.Nested(Manufacturer, required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    country_of_origin = fields.Str(required=False)
    
    total_quantity = fields.Int(required=False)
    
    added_on_store = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    meta = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    is_set = fields.Boolean(required=False)
    
    identifier = fields.Dict(required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    dimension = fields.Nested(Dimension, required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    fragile = fields.Boolean(required=False)
    
    fynd_article_code = fields.Str(required=False)
    

