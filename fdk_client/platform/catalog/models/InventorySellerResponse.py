"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












from .BrandMeta import BrandMeta















from .PriceMeta import PriceMeta



from .CompanyMeta import CompanyMeta



from .UserSerializer import UserSerializer



from .InventorySet import InventorySet



from .Trader1 import Trader1







from .ReturnConfig1 import ReturnConfig1



from .StoreMeta import StoreMeta







from .Quantities import Quantities







from .DimensionResponse import DimensionResponse



from .UserSerializer import UserSerializer







from .ManufacturerResponse import ManufacturerResponse











from .WeightResponse import WeightResponse





class InventorySellerResponse(BaseSchema):
    #  swagger.json

    
    identifier = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    country_of_origin = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    stage = fields.Str(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    trace_id = fields.Str(required=False)
    
    return_config = fields.Nested(ReturnConfig1, required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    added_on_store = fields.Str(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    fragile = fields.Boolean(required=False)
    
    is_set = fields.Boolean(required=False)
    
    expiration_date = fields.Str(required=False)
    
    raw_meta = fields.Dict(required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    total_quantity = fields.Int(required=False)
    
