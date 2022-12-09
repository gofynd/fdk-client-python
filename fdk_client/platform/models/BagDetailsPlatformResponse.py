"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Prices import Prices

from .BagMeta import BagMeta



from .BagStatusHistory import BagStatusHistory





from .Store import Store







from .BagGSTDetails import BagGSTDetails







from .AffiliateDetails import AffiliateDetails



from .Item import Item





from .Brand import Brand



from .AffiliateBagDetails import AffiliateBagDetails



from .BagStatusHistory import BagStatusHistory

from .BagStatusHistory import BagStatusHistory

from .FinancialBreakup import FinancialBreakup

from .ArticleDetails import ArticleDetails

from .BagStatusHistory import BagStatusHistory

from .Dates import Dates













from .BagReturnableCancelableStatus import BagReturnableCancelableStatus



from .Article import Article




class BagDetailsPlatformResponse(BaseSchema):
    # Order swagger.json

    
    prices = fields.Nested(Prices, required=False)
    
    meta = fields.Nested(BagMeta, required=False)
    
    operational_status = fields.Str(required=False)
    
    current_status = fields.Nested(BagStatusHistory, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
    ordering_store = fields.Nested(Store, required=False)
    
    no_of_bags_order = fields.Int(required=False)
    
    qc_required = fields.Raw(required=False)
    
    order_integration_id = fields.Str(required=False)
    
    gst_details = fields.Nested(BagGSTDetails, required=False)
    
    line_number = fields.Int(required=False)
    
    restore_coupon = fields.Boolean(required=False)
    
    b_id = fields.Int(required=False)
    
    affiliate_details = fields.Nested(AffiliateDetails, required=False)
    
    b_type = fields.Str(required=False)
    
    item = fields.Nested(Item, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    bag_update_time = fields.Float(required=False)
    
    brand = fields.Nested(Brand, required=False)
    
    quantity = fields.Float(required=False)
    
    affiliate_bag_details = fields.Nested(AffiliateBagDetails, required=False)
    
    display_name = fields.Str(required=False)
    
    bag_status_history = fields.Nested(BagStatusHistory, required=False)
    
    bag_status = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    article_details = fields.Nested(ArticleDetails, required=False)
    
    current_operational_status = fields.Nested(BagStatusHistory, required=False)
    
    dates = fields.Nested(Dates, required=False)
    
    journey_type = fields.Str(required=False)
    
    applied_promos = fields.List(fields.Dict(required=False), required=False)
    
    original_bag_list = fields.List(fields.Int(required=False), required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    entity_type = fields.Str(required=False)
    
    restore_promos = fields.Dict(required=False)
    
    status = fields.Nested(BagReturnableCancelableStatus, required=False)
    
    identifier = fields.Str(required=False)
    
    article = fields.Nested(Article, required=False)
    
    shipment_id = fields.Str(required=False)
    

