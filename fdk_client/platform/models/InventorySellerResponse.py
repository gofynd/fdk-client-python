"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Quantities import Quantities



from .StoreMeta import StoreMeta





from .Weight import Weight











from .PriceMeta import PriceMeta





from .InventorySet import InventorySet

from .Trader1 import Trader1



from .CompanyMeta import CompanyMeta





from .UserSerializer import UserSerializer

from .UserSerializer import UserSerializer

from .Manufacturer import Manufacturer

from .Dimension import Dimension















from .BrandMeta import BrandMeta


class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    track_inventory = fields.Boolean(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    size = fields.Str(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    weight = fields.Nested(Weight, required=False)
    
    uid = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    item_id = fields.Int(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    raw_meta = fields.Dict(required=False)
    
    added_on_store = fields.Str(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    identifier = fields.Dict(required=False)
    
    is_set = fields.Boolean(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    manufacturer = fields.Nested(Manufacturer, required=False)
    
    dimension = fields.Nested(Dimension, required=False)
    
    fragile = fields.Boolean(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    return_config = fields.Dict(required=False)
    
    expiration_date = fields.Str(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    total_quantity = fields.Int(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    

