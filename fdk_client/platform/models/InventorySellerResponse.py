"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PriceMeta import PriceMeta



from .CompanyMeta import CompanyMeta

from .BrandMeta import BrandMeta







from .Manufacturer import Manufacturer





from .Dimension import Dimension



from .Trader1 import Trader1







from .Weight import Weight









from .InventorySet import InventorySet

from .StoreMeta import StoreMeta



from .UserSerializer import UserSerializer









from .UserSerializer import UserSerializer

from .Quantities import Quantities






class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    price = fields.Nested(PriceMeta, required=False)
    
    item_id = fields.Int(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    uid = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    raw_meta = fields.Dict(required=False)
    
    manufacturer = fields.Nested(Manufacturer, required=False)
    
    return_config = fields.Dict(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    dimension = fields.Nested(Dimension, required=False)
    
    is_active = fields.Boolean(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    expiration_date = fields.Str(required=False)
    
    fragile = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    weight = fields.Nested(Weight, required=False)
    
    is_set = fields.Boolean(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    identifier = fields.Dict(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    added_on_store = fields.Str(required=False)
    
    total_quantity = fields.Int(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    tax_identifier = fields.Dict(required=False)
    

