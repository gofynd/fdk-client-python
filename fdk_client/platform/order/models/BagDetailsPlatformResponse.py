"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .Article import Article



from .Store import Store







from .BagGSTDetails import BagGSTDetails



from .BagMeta import BagMeta



from .AffiliateDetails import AffiliateDetails







from .Item import Item



from .ArticleDetails import ArticleDetails



from .Prices import Prices







from .Dates import Dates







from .Brand import Brand



from .BagStatusHistory import BagStatusHistory



from .FinancialBreakup import FinancialBreakup





from .AffiliateBagDetails import AffiliateBagDetails











from .BagStatusHistory import BagStatusHistory





from .BagReturnableCancelableStatus import BagReturnableCancelableStatus









from .BagStatusHistory import BagStatusHistory





from .BagStatusHistory import BagStatusHistory





class BagDetailsPlatformResponse(BaseSchema):
    #  swagger.json

    
    applied_promos = fields.List(fields.Dict(required=False), required=False)
    
    line_number = fields.Int(required=False)
    
    shipment_id = fields.Str(required=False)
    
    article = fields.Nested(Article, required=False)
    
    ordering_store = fields.Nested(Store, required=False)
    
    original_bag_list = fields.List(fields.Int(required=False), required=False)
    
    qc_required = fields.Raw(required=False)
    
    gst_details = fields.Nested(BagGSTDetails, required=False)
    
    meta = fields.Nested(BagMeta, required=False)
    
    affiliate_details = fields.Nested(AffiliateDetails, required=False)
    
    entity_type = fields.Str(required=False)
    
    restore_coupon = fields.Boolean(required=False)
    
    item = fields.Nested(Item, required=False)
    
    article_details = fields.Nested(ArticleDetails, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    no_of_bags_order = fields.Int(required=False)
    
    operational_status = fields.Str(required=False)
    
    dates = fields.Nested(Dates, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    seller_identifier = fields.Str(required=False)
    
    brand = fields.Nested(Brand, required=False)
    
    current_operational_status = fields.Nested(BagStatusHistory, required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    b_id = fields.Int(required=False)
    
    affiliate_bag_details = fields.Nested(AffiliateBagDetails, required=False)
    
    b_type = fields.Str(required=False)
    
    order_integration_id = fields.Str(required=False)
    
    journey_type = fields.Str(required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
    current_status = fields.Nested(BagStatusHistory, required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    status = fields.Nested(BagReturnableCancelableStatus, required=False)
    
    identifier = fields.Str(required=False)
    
    quantity = fields.Float(required=False)
    
    bag_update_time = fields.Float(required=False)
    
    bag_status_history = fields.Nested(BagStatusHistory, required=False)
    
    restore_promos = fields.Dict(required=False)
    
    bag_status = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    display_name = fields.Str(required=False)
    
