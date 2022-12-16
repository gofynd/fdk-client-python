"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Prices import Prices











from .BagStatusHistory import BagStatusHistory





from .BagGSTDetails import BagGSTDetails



from .ArticleDetails1 import ArticleDetails1





from .BagMeta import BagMeta





from .Dates import Dates



from .Store1 import Store1













from .Article import Article



from .BagReturnableCancelableStatus import BagReturnableCancelableStatus





from .BagStatusHistory import BagStatusHistory



from .Brand import Brand







from .BagStatusHistory import BagStatusHistory







from .FinancialBreakup import FinancialBreakup





from .BagStatusHistory import BagStatusHistory



from .AffiliateDetails import AffiliateDetails









from .Item import Item





from .AffiliateBagDetails import AffiliateBagDetails



class BagDetailsPlatformResponse(BaseSchema):
    #  swagger.json

    
    prices = fields.Nested(Prices, required=False)
    
    shipment_id = fields.Str(required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
    seller_identifier = fields.Str(required=False)
    
    bag_update_time = fields.Float(required=False)
    
    bag_status_history = fields.Nested(BagStatusHistory, required=False)
    
    order_integration_id = fields.Str(required=False)
    
    gst_details = fields.Nested(BagGSTDetails, required=False)
    
    article_details = fields.Nested(ArticleDetails1, required=False)
    
    entity_type = fields.Str(required=False)
    
    meta = fields.Nested(BagMeta, required=False)
    
    display_name = fields.Str(required=False)
    
    dates = fields.Nested(Dates, required=False)
    
    ordering_store = fields.Nested(Store1, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    b_id = fields.Int(required=False)
    
    no_of_bags_order = fields.Int(required=False)
    
    operational_status = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    article = fields.Nested(Article, required=False)
    
    status = fields.Nested(BagReturnableCancelableStatus, required=False)
    
    qc_required = fields.Raw(required=False)
    
    current_status = fields.Nested(BagStatusHistory, required=False)
    
    brand = fields.Nested(Brand, required=False)
    
    b_type = fields.Str(required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    current_operational_status = fields.Nested(BagStatusHistory, required=False)
    
    original_bag_list = fields.List(fields.Int(required=False), required=False)
    
    journey_type = fields.Str(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    line_number = fields.Int(required=False)
    
    bag_status = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    affiliate_details = fields.Nested(AffiliateDetails, required=False)
    
    restore_promos = fields.Dict(required=False)
    
    quantity = fields.Float(required=False)
    
    restore_coupon = fields.Boolean(required=False)
    
    item = fields.Nested(Item, required=False)
    
    applied_promos = fields.List(fields.Dict(required=False), required=False)
    
    affiliate_bag_details = fields.Nested(AffiliateBagDetails, required=False)
    