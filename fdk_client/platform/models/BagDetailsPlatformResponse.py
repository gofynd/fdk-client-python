"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .BagStatusHistory import BagStatusHistory

from .Prices import Prices





from .BagMeta import BagMeta

from .Item import Item



from .BagReturnableCancelableStatus import BagReturnableCancelableStatus

from .BagGSTDetails import BagGSTDetails

from .Article import Article









from .Brand import Brand



from .BagStatusHistory import BagStatusHistory

from .BagStatusHistory import BagStatusHistory

from .BagStatusHistory import BagStatusHistory

from .Dates import Dates

















from .ArticleDetails import ArticleDetails

from .AffiliateDetails import AffiliateDetails

from .FinancialBreakup import FinancialBreakup

from .AffiliateBagDetails import AffiliateBagDetails







from .Store import Store


class BagDetailsPlatformResponse(BaseSchema):
    # Order swagger.json

    
    quantity = fields.Float(required=False)
    
    applied_promos = fields.List(fields.Dict(required=False), required=False)
    
    original_bag_list = fields.List(fields.Int(required=False), required=False)
    
    current_operational_status = fields.Nested(BagStatusHistory, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    restore_coupon = fields.Boolean(required=False)
    
    restore_promos = fields.Dict(required=False)
    
    meta = fields.Nested(BagMeta, required=False)
    
    item = fields.Nested(Item, required=False)
    
    qc_required = fields.Raw(required=False)
    
    status = fields.Nested(BagReturnableCancelableStatus, required=False)
    
    gst_details = fields.Nested(BagGSTDetails, required=False)
    
    article = fields.Nested(Article, required=False)
    
    b_id = fields.Int(required=False)
    
    line_number = fields.Int(required=False)
    
    identifier = fields.Str(required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
    brand = fields.Nested(Brand, required=False)
    
    order_integration_id = fields.Str(required=False)
    
    current_status = fields.Nested(BagStatusHistory, required=False)
    
    bag_status = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    bag_status_history = fields.Nested(BagStatusHistory, required=False)
    
    dates = fields.Nested(Dates, required=False)
    
    b_type = fields.Str(required=False)
    
    no_of_bags_order = fields.Int(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    journey_type = fields.Str(required=False)
    
    operational_status = fields.Str(required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    article_details = fields.Nested(ArticleDetails, required=False)
    
    affiliate_details = fields.Nested(AffiliateDetails, required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    affiliate_bag_details = fields.Nested(AffiliateBagDetails, required=False)
    
    display_name = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    bag_update_time = fields.Float(required=False)
    
    ordering_store = fields.Nested(Store, required=False)
    

