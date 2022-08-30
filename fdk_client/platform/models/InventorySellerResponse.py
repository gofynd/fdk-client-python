"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema













from .DimensionResponse import DimensionResponse



from .BaseUserSerializerWithID import BaseUserSerializerWithID



from .BrandMeta import BrandMeta



from .BaseUserSerializerWithID import BaseUserSerializerWithID

from .Quantities import Quantities

from .CompanyMeta import CompanyMeta









from .PriceMeta import PriceMeta

from .ManufacturerResponse import ManufacturerResponse





from .ReturnConfig1 import ReturnConfig1





from .WeightResponse import WeightResponse





from .StoreMeta import StoreMeta





from .InventorySet import InventorySet



from .Trader1 import Trader1




class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    identifier = fields.Dict(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    stage = fields.Str(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    fragile = fields.Boolean(required=False)
    
    modified_by = fields.Nested(BaseUserSerializerWithID, required=False)
    
    net_quantity_unit = fields.Raw(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    created_by = fields.Nested(BaseUserSerializerWithID, required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    is_set = fields.Boolean(required=False)
    
    item_id = fields.Int(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    size = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    return_config = fields.Nested(ReturnConfig1, required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    raw_meta = fields.Dict(required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    expiration_date = fields.Str(required=False)
    
    total_quantity = fields.Int(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    added_on_store = fields.Str(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    net_quantity_value = fields.Float(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    seller_identifier = fields.Str(required=False)
    

