"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Article import Article









from .Item import Item

from .BagGSTDetails import BagGSTDetails

from .BagMeta import BagMeta





from .AffiliateBagDetails import AffiliateBagDetails

from .BagStatusHistory import BagStatusHistory

from .Brand import Brand



from .BagStatusHistory import BagStatusHistory



from .FinancialBreakup import FinancialBreakup





from .BagStatusHistory import BagStatusHistory

from .BagReturnableCancelableStatus import BagReturnableCancelableStatus

from .Prices import Prices






class Bag(BaseSchema):
    # Order swagger.json

    
    article = fields.Nested(Article, required=False)
    
    journey_type = fields.Str(required=False)
    
    b_id = fields.Int(required=False)
    
    b_type = fields.Str(required=False)
    
    dates = fields.Dict(required=False)
    
    item = fields.Nested(Item, required=False)
    
    gst_details = fields.Nested(BagGSTDetails, required=False)
    
    meta = fields.Nested(BagMeta, required=False)
    
    order_integration_id = fields.Str(required=False)
    
    applied_promos = fields.List(fields.Dict(required=False), required=False)
    
    affiliate_bag_details = fields.Nested(AffiliateBagDetails, required=False)
    
    current_status = fields.Nested(BagStatusHistory, required=False)
    
    brand = fields.Nested(Brand, required=False)
    
    bag_update_time = fields.Float(required=False)
    
    current_operational_status = fields.Nested(BagStatusHistory, required=False)
    
    entity_type = fields.Str(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    payment_methods = fields.Dict(required=False)
    
    bag_id = fields.Int(required=False)
    
    bag_status = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    status = fields.Nested(BagReturnableCancelableStatus, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
    display_name = fields.Str(required=False)
    

