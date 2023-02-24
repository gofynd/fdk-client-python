"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Brand import Brand















from .BagReturnableCancelableStatus import BagReturnableCancelableStatus

from .Item import Item







from .AffiliateDetails import AffiliateDetails









from .Article import Article



from .Store import Store

from .BagMeta import BagMeta



from .BagGSTDetails import BagGSTDetails

from .Dates import Dates

from .BagStatusHistory import BagStatusHistory

from .BagStatusHistory import BagStatusHistory





from .ArticleDetails import ArticleDetails

from .FinancialBreakup import FinancialBreakup

from .BagStatusHistory import BagStatusHistory





from .AffiliateBagDetails import AffiliateBagDetails

from .Prices import Prices



from .BagStatusHistory import BagStatusHistory




class BagDetailsPlatformResponse(BaseSchema):
    # Order swagger.json

    
    brand = fields.Nested(Brand, required=False)
    
    journey_type = fields.Str(required=False)
    
    parent_promo_bags = fields.Dict(required=False)
    
    original_bag_list = fields.List(fields.Int(required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    operational_status = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    order_integration_id = fields.Str(required=False)
    
    status = fields.Nested(BagReturnableCancelableStatus, required=False)
    
    item = fields.Nested(Item, required=False)
    
    quantity = fields.Float(required=False)
    
    b_id = fields.Int(required=False)
    
    shipment_id = fields.Str(required=False)
    
    affiliate_details = fields.Nested(AffiliateDetails, required=False)
    
    applied_promos = fields.List(fields.Dict(required=False), required=False)
    
    bag_update_time = fields.Float(required=False)
    
    display_name = fields.Str(required=False)
    
    restore_promos = fields.Dict(required=False)
    
    article = fields.Nested(Article, required=False)
    
    entity_type = fields.Str(required=False)
    
    ordering_store = fields.Nested(Store, required=False)
    
    meta = fields.Nested(BagMeta, required=False)
    
    identifier = fields.Str(required=False)
    
    gst_details = fields.Nested(BagGSTDetails, required=False)
    
    dates = fields.Nested(Dates, required=False)
    
    bag_status = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    current_operational_status = fields.Nested(BagStatusHistory, required=False)
    
    b_type = fields.Str(required=False)
    
    qc_required = fields.Raw(required=False)
    
    article_details = fields.Nested(ArticleDetails, required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    current_status = fields.Nested(BagStatusHistory, required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
    restore_coupon = fields.Boolean(required=False)
    
    affiliate_bag_details = fields.Nested(AffiliateBagDetails, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    line_number = fields.Int(required=False)
    
    bag_status_history = fields.Nested(BagStatusHistory, required=False)
    
    no_of_bags_order = fields.Int(required=False)
    

