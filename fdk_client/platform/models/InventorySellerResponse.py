"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .DimensionResponse import DimensionResponse



from .CompanyMeta import CompanyMeta

from .Trader1 import Trader1



from .PriceMeta import PriceMeta









from .BaseUserSerializerWithID import BaseUserSerializerWithID



from .InventorySet import InventorySet









from .BrandMeta import BrandMeta

from .BaseUserSerializerWithID import BaseUserSerializerWithID



from .Quantities import Quantities





from .ManufacturerResponse import ManufacturerResponse



from .WeightResponse import WeightResponse



from .StoreMeta import StoreMeta







from .ReturnConfig1 import ReturnConfig1


class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    total_quantity = fields.Int(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    net_quantity_value = fields.Float(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    fragile = fields.Boolean(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    stage = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    identifier = fields.Dict(required=False)
    
    size = fields.Str(required=False)
    
    created_by = fields.Nested(BaseUserSerializerWithID, required=False)
    
    net_quantity_unit = fields.Raw(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    item_id = fields.Int(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    expiration_date = fields.Str(required=False)
    
    raw_meta = fields.Dict(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    modified_by = fields.Nested(BaseUserSerializerWithID, required=False)
    
    added_on_store = fields.Str(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    meta = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    uid = fields.Str(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    return_config = fields.Nested(ReturnConfig1, required=False)
    

