"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ReturnConfig1 import ReturnConfig1





from .DimensionResponse import DimensionResponse







from .PriceMeta import PriceMeta







from .StoreMeta import StoreMeta



from .ManufacturerResponse import ManufacturerResponse

from .Trader1 import Trader1









from .WeightResponse import WeightResponse

from .BrandMeta import BrandMeta



from .Quantities import Quantities



from .CompanyMeta import CompanyMeta







from .BaseUserSerializerWithID import BaseUserSerializerWithID

from .InventorySet import InventorySet

from .BaseUserSerializerWithID import BaseUserSerializerWithID












class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    return_config = fields.Nested(ReturnConfig1, required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    item_id = fields.Int(required=False)
    
    fragile = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    total_quantity = fields.Int(required=False)
    
    added_on_store = fields.Str(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    meta = fields.Dict(required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    expiration_date = fields.Str(required=False)
    
    net_quantity_unit = fields.Raw(required=False)
    
    is_active = fields.Boolean(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    net_quantity_value = fields.Float(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    uid = fields.Str(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    size = fields.Str(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    raw_meta = fields.Dict(required=False)
    
    modified_by = fields.Nested(BaseUserSerializerWithID, required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    created_by = fields.Nested(BaseUserSerializerWithID, required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    stage = fields.Str(required=False)
    
    identifier = fields.Dict(required=False)
    

