"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Store import Store













from .BagStatusHistory import BagStatusHistory





from .BagReturnableCancelableStatus import BagReturnableCancelableStatus





from .Prices import Prices





from .BagStatusHistory import BagStatusHistory





from .BagMeta import BagMeta





from .BagStatusHistory import BagStatusHistory



from .ArticleDetails import ArticleDetails



from .AffiliateBagDetails import AffiliateBagDetails







from .BagStatusHistory import BagStatusHistory



from .FinancialBreakup import FinancialBreakup









from .AffiliateDetails import AffiliateDetails









from .Brand import Brand



from .Dates import Dates





from .BagGSTDetails import BagGSTDetails



from .Item import Item







from .Article import Article





class BagDetailsPlatformResponse(BaseSchema):
    #  swagger.json

    
    ordering_store = fields.Nested(Store, required=False)
    
    b_type = fields.Str(required=False)
    
    journey_type = fields.Str(required=False)
    
    line_number = fields.Int(required=False)
    
    operational_status = fields.Str(required=False)
    
    restore_coupon = fields.Boolean(required=False)
    
    bag_status_history = fields.Nested(BagStatusHistory, required=False)
    
    original_bag_list = fields.List(fields.Int(required=False), required=False)
    
    status = fields.Nested(BagReturnableCancelableStatus, required=False)
    
    qc_required = fields.Raw(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    quantity = fields.Float(required=False)
    
    current_status = fields.Nested(BagStatusHistory, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    meta = fields.Nested(BagMeta, required=False)
    
    entity_type = fields.Str(required=False)
    
    current_operational_status = fields.Nested(BagStatusHistory, required=False)
    
    article_details = fields.Nested(ArticleDetails, required=False)
    
    affiliate_bag_details = fields.Nested(AffiliateBagDetails, required=False)
    
    shipment_id = fields.Str(required=False)
    
    bag_update_time = fields.Float(required=False)
    
    bag_status = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    order_integration_id = fields.Str(required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    display_name = fields.Str(required=False)
    
    affiliate_details = fields.Nested(AffiliateDetails, required=False)
    
    applied_promos = fields.List(fields.Dict(required=False), required=False)
    
    restore_promos = fields.Dict(required=False)
    
    identifier = fields.Str(required=False)
    
    brand = fields.Nested(Brand, required=False)
    
    dates = fields.Nested(Dates, required=False)
    
    b_id = fields.Int(required=False)
    
    gst_details = fields.Nested(BagGSTDetails, required=False)
    
    item = fields.Nested(Item, required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
    no_of_bags_order = fields.Int(required=False)
    
    article = fields.Nested(Article, required=False)
    
    seller_identifier = fields.Str(required=False)
    
