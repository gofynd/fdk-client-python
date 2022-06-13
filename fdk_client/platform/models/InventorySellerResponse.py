"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .PriceMeta import PriceMeta



from .BrandMeta import BrandMeta





from .UserSerializer import UserSerializer





from .Dimension import Dimension

from .StoreMeta import StoreMeta



from .Weight import Weight

from .Quantities import Quantities





from .CompanyMeta import CompanyMeta





from .InventorySet import InventorySet





from .Manufacturer import Manufacturer







from .UserSerializer import UserSerializer

from .Trader1 import Trader1








class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    seller_identifier = fields.Str(required=False)
    
    return_config = fields.Dict(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    expiration_date = fields.Str(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    fragile = fields.Boolean(required=False)
    
    added_on_store = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    identifier = fields.Dict(required=False)
    
    item_id = fields.Int(required=False)
    
    dimension = fields.Nested(Dimension, required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    weight = fields.Nested(Weight, required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    uid = fields.Str(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    raw_meta = fields.Dict(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    total_quantity = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    manufacturer = fields.Nested(Manufacturer, required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    size = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    

