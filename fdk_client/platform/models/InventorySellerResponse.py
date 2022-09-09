"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PriceMeta import PriceMeta









from .WeightResponse import WeightResponse





from .BaseUserSerializerWithID import BaseUserSerializerWithID



from .DimensionResponse import DimensionResponse



from .ReturnConfig1 import ReturnConfig1













from .BrandMeta import BrandMeta

from .CompanyMeta import CompanyMeta



from .ManufacturerResponse import ManufacturerResponse

from .StoreMeta import StoreMeta



from .InventorySet import InventorySet



from .Quantities import Quantities

from .Trader1 import Trader1





from .BaseUserSerializerWithID import BaseUserSerializerWithID










class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    price = fields.Nested(PriceMeta, required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    raw_meta = fields.Dict(required=False)
    
    total_quantity = fields.Int(required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    uid = fields.Str(required=False)
    
    expiration_date = fields.Str(required=False)
    
    created_by = fields.Nested(BaseUserSerializerWithID, required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    size = fields.Str(required=False)
    
    return_config = fields.Nested(ReturnConfig1, required=False)
    
    meta = fields.Dict(required=False)
    
    net_quantity_value = fields.Float(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    item_id = fields.Int(required=False)
    
    net_quantity_unit = fields.Raw(required=False)
    
    identifier = fields.Dict(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    is_active = fields.Boolean(required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    is_set = fields.Boolean(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    country_of_origin = fields.Str(required=False)
    
    fragile = fields.Boolean(required=False)
    
    modified_by = fields.Nested(BaseUserSerializerWithID, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    added_on_store = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    fynd_meta = fields.Dict(required=False)
    

