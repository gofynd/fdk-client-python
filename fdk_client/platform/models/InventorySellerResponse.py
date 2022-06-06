"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Weight import Weight









from .CompanyMeta import CompanyMeta







from .InventorySet import InventorySet















from .UserSerializer import UserSerializer



from .BrandMeta import BrandMeta

from .Quantities import Quantities





from .Manufacturer import Manufacturer

from .UserSerializer import UserSerializer



from .StoreMeta import StoreMeta

from .Dimension import Dimension



from .PriceMeta import PriceMeta

from .Trader1 import Trader1






class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    weight = fields.Nested(Weight, required=False)
    
    uid = fields.Str(required=False)
    
    fragile = fields.Boolean(required=False)
    
    return_config = fields.Dict(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    is_set = fields.Boolean(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    added_on_store = fields.Str(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    expiration_date = fields.Str(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    is_active = fields.Boolean(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    raw_meta = fields.Dict(required=False)
    
    manufacturer = fields.Nested(Manufacturer, required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    identifier = fields.Dict(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    dimension = fields.Nested(Dimension, required=False)
    
    item_id = fields.Int(required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    size = fields.Str(required=False)
    
    total_quantity = fields.Int(required=False)
    

