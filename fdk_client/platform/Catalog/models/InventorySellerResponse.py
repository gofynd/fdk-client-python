"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .UserSerializer import UserSerializer











from .Trader1 import Trader1



from .UserSerializer import UserSerializer



from .CompanyMeta import CompanyMeta







from .Quantities import Quantities



from .WeightResponse import WeightResponse























from .PriceMeta import PriceMeta



from .ReturnConfig1 import ReturnConfig1





from .InventorySet import InventorySet



from .StoreMeta import StoreMeta



from .ManufacturerResponse import ManufacturerResponse



from .BrandMeta import BrandMeta







from .DimensionResponse import DimensionResponse









class InventorySellerResponse(BaseSchema):
    #  swagger.json

    
    created_by = fields.Nested(UserSerializer, required=False)
    
    raw_meta = fields.Dict(required=False)
    
    total_quantity = fields.Int(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    country_of_origin = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    expiration_date = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    identifier = fields.Dict(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    added_on_store = fields.Str(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    return_config = fields.Nested(ReturnConfig1, required=False)
    
    size = fields.Str(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    fragile = fields.Boolean(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    is_set = fields.Boolean(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    seller_identifier = fields.Str(required=False)
    
