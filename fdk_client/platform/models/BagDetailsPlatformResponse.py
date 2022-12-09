"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .BagReturnableCancelableStatus import BagReturnableCancelableStatus

from .Dates import Dates



from .AffiliateBagDetails import AffiliateBagDetails



from .AffiliateDetails import AffiliateDetails

















from .BagStatusHistory import BagStatusHistory

from .BagGSTDetails import BagGSTDetails

from .Item import Item

from .BagStatusHistory import BagStatusHistory







from .Article import Article

from .BagStatusHistory import BagStatusHistory









from .Brand import Brand

from .FinancialBreakup import FinancialBreakup



from .Prices import Prices

from .BagStatusHistory import BagStatusHistory





from .ArticleDetails import ArticleDetails



from .BagMeta import BagMeta

from .Store import Store


class BagDetailsPlatformResponse(BaseSchema):
    # Order swagger.json

    
    b_id = fields.Int(required=False)
    
    status = fields.Nested(BagReturnableCancelableStatus, required=False)
    
    dates = fields.Nested(Dates, required=False)
    
    restore_coupon = fields.Boolean(required=False)
    
    affiliate_bag_details = fields.Nested(AffiliateBagDetails, required=False)
    
    b_type = fields.Str(required=False)
    
    affiliate_details = fields.Nested(AffiliateDetails, required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
    identifier = fields.Str(required=False)
    
    restore_promos = fields.Dict(required=False)
    
    display_name = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    journey_type = fields.Str(required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    line_number = fields.Int(required=False)
    
    bag_status = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    gst_details = fields.Nested(BagGSTDetails, required=False)
    
    item = fields.Nested(Item, required=False)
    
    current_status = fields.Nested(BagStatusHistory, required=False)
    
    qc_required = fields.Raw(required=False)
    
    applied_promos = fields.List(fields.Dict(required=False), required=False)
    
    no_of_bags_order = fields.Int(required=False)
    
    article = fields.Nested(Article, required=False)
    
    bag_status_history = fields.Nested(BagStatusHistory, required=False)
    
    original_bag_list = fields.List(fields.Int(required=False), required=False)
    
    operational_status = fields.Str(required=False)
    
    bag_update_time = fields.Float(required=False)
    
    shipment_id = fields.Str(required=False)
    
    brand = fields.Nested(Brand, required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    quantity = fields.Float(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    current_operational_status = fields.Nested(BagStatusHistory, required=False)
    
    entity_type = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    article_details = fields.Nested(ArticleDetails, required=False)
    
    order_integration_id = fields.Str(required=False)
    
    meta = fields.Nested(BagMeta, required=False)
    
    ordering_store = fields.Nested(Store, required=False)
    

