"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .AffiliateConfig1 import AffiliateConfig1

from .ShipmentMeta import ShipmentMeta









from .PDFLinks import PDFLinks



from .AffiliateMeta import AffiliateMeta


class AffiliateDetails(BaseSchema):
    # Order swagger.json

    
    affiliate_bag_id = fields.Str(required=False)
    
    affiliate_id = fields.Str(required=False)
    
    config = fields.Nested(AffiliateConfig1, required=False)
    
    shipment_meta = fields.Nested(ShipmentMeta, required=False)
    
    affiliate_shipment_id = fields.Str(required=False)
    
    company_affiliate_tag = fields.Str(required=False)
    
    ad_id = fields.Str(required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    pdf_links = fields.Nested(PDFLinks, required=False)
    
    affiliate_store_id = fields.Str(required=False)
    
    affiliate_meta = fields.Nested(AffiliateMeta, required=False)
    

