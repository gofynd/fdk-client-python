"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .BagStatusHistory import BagStatusHistory

from .BagStatusHistory import BagStatusHistory



from .Store import Store







from .BagGSTDetails import BagGSTDetails

from .AffiliateBagDetails import AffiliateBagDetails







from .BagStatusHistory import BagStatusHistory



from .FinancialBreakup import FinancialBreakup





from .Dates import Dates

from .BagMeta import BagMeta



from .AffiliateDetails import AffiliateDetails

from .Article import Article



from .BagStatusHistory import BagStatusHistory









from .Item import Item





from .Brand import Brand



from .ArticleDetails import ArticleDetails



from .Prices import Prices



from .BagReturnableCancelableStatus import BagReturnableCancelableStatus


class BagDetailsPlatformResponse(BaseSchema):
    # Orders swagger.json

    
    bag_update_time = fields.Float(required=False)
    
    current_operational_status = fields.Nested(BagStatusHistory, required=False)
    
    current_status = fields.Nested(BagStatusHistory, required=False)
    
    order_integration_id = fields.Str(required=False)
    
    ordering_store = fields.Nested(Store, required=False)
    
    restore_coupon = fields.Boolean(required=False)
    
    entity_type = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    gst_details = fields.Nested(BagGSTDetails, required=False)
    
    affiliate_bag_details = fields.Nested(AffiliateBagDetails, required=False)
    
    original_bag_list = fields.List(fields.Int(required=False), required=False)
    
    journey_type = fields.Str(required=False)
    
    b_id = fields.Int(required=False)
    
    bag_status_history = fields.Nested(BagStatusHistory, required=False)
    
    restore_promos = fields.Dict(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    qc_required = fields.Raw(required=False)
    
    quantity = fields.Float(required=False)
    
    dates = fields.Nested(Dates, required=False)
    
    meta = fields.Nested(BagMeta, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    affiliate_details = fields.Nested(AffiliateDetails, required=False)
    
    article = fields.Nested(Article, required=False)
    
    applied_promos = fields.List(fields.Dict(required=False), required=False)
    
    bag_status = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    b_type = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    item = fields.Nested(Item, required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
    shipment_id = fields.Str(required=False)
    
    brand = fields.Nested(Brand, required=False)
    
    line_number = fields.Int(required=False)
    
    article_details = fields.Nested(ArticleDetails, required=False)
    
    operational_status = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    no_of_bags_order = fields.Int(required=False)
    
    status = fields.Nested(BagReturnableCancelableStatus, required=False)
    

