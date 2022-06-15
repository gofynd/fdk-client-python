"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema













from .UserSerializer import UserSerializer

from .CompanyMeta import CompanyMeta

from .Trader1 import Trader1









from .BrandMeta import BrandMeta

from .Manufacturer import Manufacturer





from .Weight import Weight

from .Dimension import Dimension



from .InventorySet import InventorySet





from .UserSerializer import UserSerializer





from .Quantities import Quantities









from .StoreMeta import StoreMeta

from .PriceMeta import PriceMeta


class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    fynd_item_code = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    identifier = fields.Dict(required=False)
    
    fragile = fields.Boolean(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    added_on_store = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    manufacturer = fields.Nested(Manufacturer, required=False)
    
    uid = fields.Str(required=False)
    
    total_quantity = fields.Int(required=False)
    
    weight = fields.Nested(Weight, required=False)
    
    dimension = fields.Nested(Dimension, required=False)
    
    expiration_date = fields.Str(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    is_set = fields.Boolean(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    item_id = fields.Int(required=False)
    
    raw_meta = fields.Dict(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    return_config = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    

