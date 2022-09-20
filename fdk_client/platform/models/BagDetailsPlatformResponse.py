"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .BagStatusHistory import BagStatusHistory





from .BagStatusHistory import BagStatusHistory

from .FinancialBreakup import FinancialBreakup





from .Prices import Prices







from .BagGSTDetails import BagGSTDetails





from .BagStatusHistory import BagStatusHistory

from .AffiliateBagDetails import AffiliateBagDetails

from .Item import Item

from .Article import Article

from .Brand import Brand

from .BagReturnableCancelableStatus import BagReturnableCancelableStatus

from .BagMeta import BagMeta








class BagDetailsPlatformResponse(BaseSchema):
    # Order swagger.json

    
    current_status = fields.Nested(BagStatusHistory, required=False)
    
    dates = fields.Dict(required=False)
    
    bag_update_time = fields.Float(required=False)
    
    bag_status = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    journey_type = fields.Str(required=False)
    
    payment_methods = fields.Dict(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    applied_promos = fields.List(fields.Dict(required=False), required=False)
    
    display_name = fields.Str(required=False)
    
    order_integration_id = fields.Str(required=False)
    
    gst_details = fields.Nested(BagGSTDetails, required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
    entity_type = fields.Str(required=False)
    
    current_operational_status = fields.Nested(BagStatusHistory, required=False)
    
    affiliate_bag_details = fields.Nested(AffiliateBagDetails, required=False)
    
    item = fields.Nested(Item, required=False)
    
    article = fields.Nested(Article, required=False)
    
    brand = fields.Nested(Brand, required=False)
    
    status = fields.Nested(BagReturnableCancelableStatus, required=False)
    
    meta = fields.Nested(BagMeta, required=False)
    
    b_id = fields.Int(required=False)
    
    b_type = fields.Str(required=False)
    
    bag_id = fields.Int(required=False)
    

