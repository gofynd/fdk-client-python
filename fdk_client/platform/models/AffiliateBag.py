"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .MarketPlacePdf import MarketPlacePdf










































class AffiliateBag(BaseSchema):
    # Order swagger.json

    
    store_id = fields.Int(required=False)
    
    fynd_store_id = fields.Str(required=False)
    
    pdf_links = fields.Nested(MarketPlacePdf, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    affiliate_meta = fields.Dict(required=False)
    
    unit_price = fields.Float(required=False)
    
    delivery_charge = fields.Float(required=False)
    
    identifier = fields.Dict(required=False)
    
    price_marked = fields.Float(required=False)
    
    hsn_code_id = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    amount_paid = fields.Float(required=False)
    
    sku = fields.Str(required=False)
    
    item_size = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    discount = fields.Float(required=False)
    
    price_effective = fields.Float(required=False)
    
    _id = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    transfer_price = fields.Int(required=False)
    
    avl_qty = fields.Int(required=False)
    
    modified_on = fields.Str(required=False)
    
    affiliate_store_id = fields.Str(required=False)
    

