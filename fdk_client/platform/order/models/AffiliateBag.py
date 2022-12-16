"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


































from .MarketPlacePdf import MarketPlacePdf

















class AffiliateBag(BaseSchema):
    #  swagger.json

    
    quantity = fields.Int(required=False)
    
    _id = fields.Str(required=False)
    
    item_size = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    item_id = fields.Int(required=False)
    
    store_id = fields.Int(required=False)
    
    price_effective = fields.Float(required=False)
    
    identifier = fields.Dict(required=False)
    
    sku = fields.Str(required=False)
    
    transfer_price = fields.Int(required=False)
    
    modified_on = fields.Str(required=False)
    
    amount_paid = fields.Float(required=False)
    
    unit_price = fields.Float(required=False)
    
    price_marked = fields.Float(required=False)
    
    hsn_code_id = fields.Str(required=False)
    
    pdf_links = fields.Nested(MarketPlacePdf, required=False)
    
    delivery_charge = fields.Float(required=False)
    
    avl_qty = fields.Int(required=False)
    
    affiliate_store_id = fields.Str(required=False)
    
    fynd_store_id = fields.Str(required=False)
    
    affiliate_meta = fields.Dict(required=False)
    
    discount = fields.Float(required=False)
    
    seller_identifier = fields.Str(required=False)
    