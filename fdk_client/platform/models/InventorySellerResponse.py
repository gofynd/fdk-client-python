"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PriceMeta import PriceMeta

from .BrandMeta import BrandMeta



from .UserSerializer import UserSerializer

from .WeightResponse import WeightResponse







from .Quantities import Quantities



from .ManufacturerResponse import ManufacturerResponse









from .StoreMeta import StoreMeta

from .CompanyMeta import CompanyMeta







from .DimensionResponse import DimensionResponse







from .InventorySet import InventorySet



from .UserSerializer import UserSerializer









from .Trader1 import Trader1




class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    price = fields.Nested(PriceMeta, required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    raw_meta = fields.Dict(required=False)
    
    size = fields.Str(required=False)
    
    fragile = fields.Boolean(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    return_config = fields.Dict(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    item_id = fields.Int(required=False)
    
    total_quantity = fields.Int(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    is_active = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    added_on_store = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    identifier = fields.Dict(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    expiration_date = fields.Str(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    country_of_origin = fields.Str(required=False)
    

