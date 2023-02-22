"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Dates import Dates





from .AffiliateDetails import AffiliateDetails



from .Brand import Brand





from .Item import Item







from .BagStatusHistory import BagStatusHistory





from .BagStatusHistory import BagStatusHistory









from .Article import Article



from .Prices import Prices



from .BagMeta import BagMeta











from .AffiliateBagDetails import AffiliateBagDetails



from .ArticleDetails import ArticleDetails





from .Store import Store











from .BagStatusHistory import BagStatusHistory





from .BagStatusHistory import BagStatusHistory



from .FinancialBreakup import FinancialBreakup



from .BagReturnableCancelableStatus import BagReturnableCancelableStatus







from .BagGSTDetails import BagGSTDetails







class BagDetailsPlatformResponse(BaseSchema):
    #  swagger.json

    
    dates = fields.Nested(Dates, required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
    affiliate_details = fields.Nested(AffiliateDetails, required=False)
    
    brand = fields.Nested(Brand, required=False)
    
    order_integration_id = fields.Str(required=False)
    
    item = fields.Nested(Item, required=False)
    
    original_bag_list = fields.List(fields.Int(required=False), required=False)
    
    b_id = fields.Int(required=False)
    
    bag_status = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    line_number = fields.Int(required=False)
    
    current_status = fields.Nested(BagStatusHistory, required=False)
    
    applied_promos = fields.List(fields.Dict(required=False), required=False)
    
    b_type = fields.Str(required=False)
    
    restore_promos = fields.Dict(required=False)
    
    article = fields.Nested(Article, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    meta = fields.Nested(BagMeta, required=False)
    
    quantity = fields.Float(required=False)
    
    qc_required = fields.Raw(required=False)
    
    shipment_id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    affiliate_bag_details = fields.Nested(AffiliateBagDetails, required=False)
    
    article_details = fields.Nested(ArticleDetails, required=False)
    
    operational_status = fields.Str(required=False)
    
    ordering_store = fields.Nested(Store, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    identifier = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    no_of_bags_order = fields.Int(required=False)
    
    bag_status_history = fields.Nested(BagStatusHistory, required=False)
    
    restore_coupon = fields.Boolean(required=False)
    
    current_operational_status = fields.Nested(BagStatusHistory, required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    status = fields.Nested(BagReturnableCancelableStatus, required=False)
    
    journey_type = fields.Str(required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    gst_details = fields.Nested(BagGSTDetails, required=False)
    
    bag_update_time = fields.Float(required=False)
    
    display_name = fields.Str(required=False)
    
