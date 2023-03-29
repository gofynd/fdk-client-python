"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Article import Article

from .BagReturnableCancelableStatus import BagReturnableCancelableStatus

from .AffiliateDetails import AffiliateDetails



from .Store import Store

from .FinancialBreakup import FinancialBreakup

from .Dates import Dates

from .ArticleDetails import ArticleDetails









from .Prices import Prices



from .Brand import Brand

from .BagStatusHistory import BagStatusHistory

from .BagStatusHistory import BagStatusHistory

from .BagGSTDetails import BagGSTDetails



from .BagStatusHistory import BagStatusHistory













from .BagMeta import BagMeta









from .AffiliateBagDetails import AffiliateBagDetails











from .Item import Item

from .BagStatusHistory import BagStatusHistory


class BagDetailsPlatformResponse(BaseSchema):
    # Order swagger.json

    
    article = fields.Nested(Article, required=False)
    
    status = fields.Nested(BagReturnableCancelableStatus, required=False)
    
    affiliate_details = fields.Nested(AffiliateDetails, required=False)
    
    operational_status = fields.Str(required=False)
    
    ordering_store = fields.Nested(Store, required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    dates = fields.Nested(Dates, required=False)
    
    article_details = fields.Nested(ArticleDetails, required=False)
    
    qc_required = fields.Raw(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    original_bag_list = fields.List(fields.Int(required=False), required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    shipment_id = fields.Str(required=False)
    
    brand = fields.Nested(Brand, required=False)
    
    bag_status = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    current_operational_status = fields.Nested(BagStatusHistory, required=False)
    
    gst_details = fields.Nested(BagGSTDetails, required=False)
    
    restore_coupon = fields.Boolean(required=False)
    
    bag_status_history = fields.Nested(BagStatusHistory, required=False)
    
    order_integration_id = fields.Str(required=False)
    
    no_of_bags_order = fields.Int(required=False)
    
    applied_promos = fields.List(fields.Dict(required=False), required=False)
    
    bag_update_time = fields.Float(required=False)
    
    b_id = fields.Int(required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    meta = fields.Nested(BagMeta, required=False)
    
    line_number = fields.Int(required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
    quantity = fields.Float(required=False)
    
    restore_promos = fields.Dict(required=False)
    
    affiliate_bag_details = fields.Nested(AffiliateBagDetails, required=False)
    
    b_type = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    entity_type = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    journey_type = fields.Str(required=False)
    
    item = fields.Nested(Item, required=False)
    
    current_status = fields.Nested(BagStatusHistory, required=False)
    

