"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .InventorySet import InventorySet





from .Quantities import Quantities









from .StoreMeta import StoreMeta

from .BrandMeta import BrandMeta

from .UserSerializer import UserSerializer











from .UserSerializer import UserSerializer

from .Manufacturer import Manufacturer







from .Trader1 import Trader1

from .PriceMeta import PriceMeta





from .CompanyMeta import CompanyMeta



from .Dimension import Dimension



from .Weight import Weight






class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    total_quantity = fields.Int(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    return_config = fields.Dict(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    added_on_store = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    expiration_date = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    identifier = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    manufacturer = fields.Nested(Manufacturer, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    item_id = fields.Int(required=False)
    
    fragile = fields.Boolean(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    is_active = fields.Boolean(required=False)
    
    dimension = fields.Nested(Dimension, required=False)
    
    raw_meta = fields.Dict(required=False)
    
    weight = fields.Nested(Weight, required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    

