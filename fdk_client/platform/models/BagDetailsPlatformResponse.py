"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Article import Article

from .Item import Item

from .Prices import Prices





from .BagReturnableCancelableStatus import BagReturnableCancelableStatus







from .BagStatusHistory import BagStatusHistory









from .AffiliateDetails import AffiliateDetails

from .AffiliateBagDetails import AffiliateBagDetails





from .BagStatusHistory import BagStatusHistory





from .FinancialBreakup import FinancialBreakup

from .BagStatusHistory import BagStatusHistory

from .BagMeta import BagMeta





from .Store import Store

from .ArticleDetails import ArticleDetails

from .BagStatusHistory import BagStatusHistory





from .Brand import Brand

from .Dates import Dates







from .BagGSTDetails import BagGSTDetails






class BagDetailsPlatformResponse(BaseSchema):
    # Order swagger.json

    
    article = fields.Nested(Article, required=False)
    
    item = fields.Nested(Item, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    order_integration_id = fields.Str(required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
    status = fields.Nested(BagReturnableCancelableStatus, required=False)
    
    entity_type = fields.Str(required=False)
    
    applied_promos = fields.List(fields.Dict(required=False), required=False)
    
    seller_identifier = fields.Str(required=False)
    
    current_status = fields.Nested(BagStatusHistory, required=False)
    
    no_of_bags_order = fields.Int(required=False)
    
    shipment_id = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    qc_required = fields.Raw(required=False)
    
    affiliate_details = fields.Nested(AffiliateDetails, required=False)
    
    affiliate_bag_details = fields.Nested(AffiliateBagDetails, required=False)
    
    original_bag_list = fields.List(fields.Int(required=False), required=False)
    
    b_id = fields.Int(required=False)
    
    bag_status_history = fields.Nested(BagStatusHistory, required=False)
    
    restore_promos = fields.Dict(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    bag_status = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    meta = fields.Nested(BagMeta, required=False)
    
    journey_type = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    ordering_store = fields.Nested(Store, required=False)
    
    article_details = fields.Nested(ArticleDetails, required=False)
    
    current_operational_status = fields.Nested(BagStatusHistory, required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    operational_status = fields.Str(required=False)
    
    brand = fields.Nested(Brand, required=False)
    
    dates = fields.Nested(Dates, required=False)
    
    quantity = fields.Float(required=False)
    
    restore_coupon = fields.Boolean(required=False)
    
    bag_update_time = fields.Float(required=False)
    
    gst_details = fields.Nested(BagGSTDetails, required=False)
    
    b_type = fields.Str(required=False)
    
    line_number = fields.Int(required=False)
    

