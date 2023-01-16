"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .BagReturnableCancelableStatus import BagReturnableCancelableStatus



from .Dates import Dates



from .AffiliateDetails import AffiliateDetails







from .FinancialBreakup import FinancialBreakup





from .AffiliateBagDetails import AffiliateBagDetails





from .Article import Article













from .BagStatusHistory import BagStatusHistory



from .BagStatusHistory import BagStatusHistory



from .BagStatusHistory import BagStatusHistory



from .BagGSTDetails import BagGSTDetails













from .Brand import Brand



from .Item import Item



from .BagStatusHistory import BagStatusHistory



from .ArticleDetails1 import ArticleDetails1





from .Prices import Prices









from .BagMeta import BagMeta







from .Store import Store



class BagDetailsPlatformResponse(BaseSchema):
    #  swagger.json

    
    bag_update_time = fields.Float(required=False)
    
    original_bag_list = fields.List(fields.Int(required=False), required=False)
    
    status = fields.Nested(BagReturnableCancelableStatus, required=False)
    
    dates = fields.Nested(Dates, required=False)
    
    affiliate_details = fields.Nested(AffiliateDetails, required=False)
    
    qc_required = fields.Raw(required=False)
    
    no_of_bags_order = fields.Int(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    restore_promos = fields.Dict(required=False)
    
    affiliate_bag_details = fields.Nested(AffiliateBagDetails, required=False)
    
    entity_type = fields.Str(required=False)
    
    article = fields.Nested(Article, required=False)
    
    identifier = fields.Str(required=False)
    
    operational_status = fields.Str(required=False)
    
    order_integration_id = fields.Str(required=False)
    
    journey_type = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    current_operational_status = fields.Nested(BagStatusHistory, required=False)
    
    current_status = fields.Nested(BagStatusHistory, required=False)
    
    bag_status = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    gst_details = fields.Nested(BagGSTDetails, required=False)
    
    applied_promos = fields.List(fields.Dict(required=False), required=False)
    
    display_name = fields.Str(required=False)
    
    line_number = fields.Int(required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
    brand = fields.Nested(Brand, required=False)
    
    item = fields.Nested(Item, required=False)
    
    bag_status_history = fields.Nested(BagStatusHistory, required=False)
    
    article_details = fields.Nested(ArticleDetails1, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    b_type = fields.Str(required=False)
    
    b_id = fields.Int(required=False)
    
    restore_coupon = fields.Boolean(required=False)
    
    meta = fields.Nested(BagMeta, required=False)
    
    shipment_id = fields.Str(required=False)
    
    quantity = fields.Float(required=False)
    
    ordering_store = fields.Nested(Store, required=False)
    
