"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




























from .MarketPlacePdf import MarketPlacePdf























class AffiliateBag(BaseSchema):
    #  swagger.json

    
    sku = fields.Str(required=False)
    
    fynd_store_id = fields.Str(required=False)
    
    affiliate_store_id = fields.Str(required=False)
    
    unit_price = fields.Float(required=False)
    
    identifier = fields.Dict(required=False)
    
    amount_paid = fields.Float(required=False)
    
    item_id = fields.Int(required=False)
    
    store_id = fields.Int(required=False)
    
    _id = fields.Str(required=False)
    
    item_size = fields.Str(required=False)
    
    transfer_price = fields.Int(required=False)
    
    discount = fields.Float(required=False)
    
    pdf_links = fields.Nested(MarketPlacePdf, required=False)
    
    affiliate_meta = fields.Dict(required=False)
    
    price_effective = fields.Float(required=False)
    
    price_marked = fields.Float(required=False)
    
    modified_on = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    hsn_code_id = fields.Str(required=False)
    
    delivery_charge = fields.Float(required=False)
    
    avl_qty = fields.Int(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
