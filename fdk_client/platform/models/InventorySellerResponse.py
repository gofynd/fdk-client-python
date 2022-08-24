"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .WeightResponse import WeightResponse

from .StoreMeta import StoreMeta





from .ManufacturerResponse import ManufacturerResponse







from .UserSerializer import UserSerializer















from .Trader1 import Trader1



from .DimensionResponse import DimensionResponse











from .ReturnConfig1 import ReturnConfig1



from .InventorySet import InventorySet



from .UserSerializer import UserSerializer



from .Quantities import Quantities

from .CompanyMeta import CompanyMeta

from .BrandMeta import BrandMeta

from .PriceMeta import PriceMeta


class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    weight = fields.Nested(WeightResponse, required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    raw_meta = fields.Dict(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    identifier = fields.Dict(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    total_quantity = fields.Int(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    item_id = fields.Int(required=False)
    
    added_on_store = fields.Str(required=False)
    
    fragile = fields.Boolean(required=False)
    
    expiration_date = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    return_config = fields.Nested(ReturnConfig1, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    size = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    is_active = fields.Boolean(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    

