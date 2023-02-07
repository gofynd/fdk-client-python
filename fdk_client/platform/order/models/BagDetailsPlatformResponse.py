"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ArticleDetails import ArticleDetails









from .BagStatusHistory import BagStatusHistory



from .Article import Article



















from .AffiliateBagDetails import AffiliateBagDetails







from .BagReturnableCancelableStatus import BagReturnableCancelableStatus



from .BagMeta import BagMeta





from .BagStatusHistory import BagStatusHistory









from .BagStatusHistory import BagStatusHistory







from .Brand import Brand



from .Prices import Prices



from .Item import Item





from .BagStatusHistory import BagStatusHistory





from .Dates import Dates



from .FinancialBreakup import FinancialBreakup



from .BagGSTDetails import BagGSTDetails



from .AffiliateDetails import AffiliateDetails





from .Store import Store



class BagDetailsPlatformResponse(BaseSchema):
    #  swagger.json

    
    article_details = fields.Nested(ArticleDetails, required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
    b_id = fields.Int(required=False)
    
    applied_promos = fields.List(fields.Dict(required=False), required=False)
    
    bag_status_history = fields.Nested(BagStatusHistory, required=False)
    
    article = fields.Nested(Article, required=False)
    
    order_integration_id = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    shipment_id = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    quantity = fields.Float(required=False)
    
    affiliate_bag_details = fields.Nested(AffiliateBagDetails, required=False)
    
    display_name = fields.Str(required=False)
    
    qc_required = fields.Raw(required=False)
    
    status = fields.Nested(BagReturnableCancelableStatus, required=False)
    
    meta = fields.Nested(BagMeta, required=False)
    
    operational_status = fields.Str(required=False)
    
    bag_status = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    line_number = fields.Int(required=False)
    
    original_bag_list = fields.List(fields.Int(required=False), required=False)
    
    journey_type = fields.Str(required=False)
    
    current_operational_status = fields.Nested(BagStatusHistory, required=False)
    
    bag_update_time = fields.Float(required=False)
    
    b_type = fields.Str(required=False)
    
    brand = fields.Nested(Brand, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    item = fields.Nested(Item, required=False)
    
    restore_coupon = fields.Boolean(required=False)
    
    current_status = fields.Nested(BagStatusHistory, required=False)
    
    no_of_bags_order = fields.Int(required=False)
    
    dates = fields.Nested(Dates, required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    gst_details = fields.Nested(BagGSTDetails, required=False)
    
    affiliate_details = fields.Nested(AffiliateDetails, required=False)
    
    restore_promos = fields.Dict(required=False)
    
    ordering_store = fields.Nested(Store, required=False)
    
