"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Dates import Dates

from .ArticleDetails import ArticleDetails











from .BagStatusHistory import BagStatusHistory

from .BagReturnableCancelableStatus import BagReturnableCancelableStatus







from .Store import Store





from .AffiliateBagDetails import AffiliateBagDetails

from .AffiliateDetails import AffiliateDetails

from .Item import Item







from .FinancialBreakup import FinancialBreakup

from .Article import Article

from .BagStatusHistory import BagStatusHistory



from .Prices import Prices

from .BagGSTDetails import BagGSTDetails

from .BagMeta import BagMeta







from .Brand import Brand



from .BagStatusHistory import BagStatusHistory

from .BagStatusHistory import BagStatusHistory








class BagDetailsPlatformResponse(BaseSchema):
    # Order swagger.json

    
    qc_required = fields.Raw(required=False)
    
    dates = fields.Nested(Dates, required=False)
    
    article_details = fields.Nested(ArticleDetails, required=False)
    
    journey_type = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    quantity = fields.Float(required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    applied_promos = fields.List(fields.Dict(required=False), required=False)
    
    current_status = fields.Nested(BagStatusHistory, required=False)
    
    status = fields.Nested(BagReturnableCancelableStatus, required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
    entity_type = fields.Str(required=False)
    
    line_number = fields.Int(required=False)
    
    ordering_store = fields.Nested(Store, required=False)
    
    bag_update_time = fields.Float(required=False)
    
    no_of_bags_order = fields.Int(required=False)
    
    affiliate_bag_details = fields.Nested(AffiliateBagDetails, required=False)
    
    affiliate_details = fields.Nested(AffiliateDetails, required=False)
    
    item = fields.Nested(Item, required=False)
    
    b_id = fields.Int(required=False)
    
    restore_coupon = fields.Boolean(required=False)
    
    display_name = fields.Str(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    article = fields.Nested(Article, required=False)
    
    bag_status_history = fields.Nested(BagStatusHistory, required=False)
    
    operational_status = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    gst_details = fields.Nested(BagGSTDetails, required=False)
    
    meta = fields.Nested(BagMeta, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    restore_promos = fields.Dict(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    brand = fields.Nested(Brand, required=False)
    
    original_bag_list = fields.List(fields.Int(required=False), required=False)
    
    current_operational_status = fields.Nested(BagStatusHistory, required=False)
    
    bag_status = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    shipment_id = fields.Str(required=False)
    
    b_type = fields.Str(required=False)
    
    order_integration_id = fields.Str(required=False)
    

