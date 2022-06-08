"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .Weight import Weight



from .Quantities import Quantities









from .Dimension import Dimension

from .UserSerializer import UserSerializer

from .PriceMeta import PriceMeta



from .InventorySet import InventorySet











from .Trader1 import Trader1







from .BrandMeta import BrandMeta

from .Manufacturer import Manufacturer



from .StoreMeta import StoreMeta



from .UserSerializer import UserSerializer



from .CompanyMeta import CompanyMeta


class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    identifier = fields.Dict(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    item_id = fields.Int(required=False)
    
    weight = fields.Nested(Weight, required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    size = fields.Str(required=False)
    
    return_config = fields.Dict(required=False)
    
    added_on_store = fields.Str(required=False)
    
    dimension = fields.Nested(Dimension, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    expiration_date = fields.Str(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_set = fields.Boolean(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    raw_meta = fields.Dict(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    fragile = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    manufacturer = fields.Nested(Manufacturer, required=False)
    
    country_of_origin = fields.Str(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    total_quantity = fields.Int(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    

