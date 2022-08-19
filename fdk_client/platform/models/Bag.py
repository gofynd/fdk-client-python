"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Prices import Prices





from .FinancialBreakup import FinancialBreakup

from .Item import Item

from .BagMeta import BagMeta

from .Brand import Brand



from .BagGSTDetails import BagGSTDetails



from .BagStatusHistory import BagStatusHistory



from .Article import Article







from .AffiliateBagDetails import AffiliateBagDetails





from .BagReturnableCancelableStatus import BagReturnableCancelableStatus

from .BagStatusHistory import BagStatusHistory

from .BagStatusHistory import BagStatusHistory




class Bag(BaseSchema):
    # Order swagger.json

    
    order_integration_id = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    bag_update_time = fields.Float(required=False)
    
    b_type = fields.Str(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    item = fields.Nested(Item, required=False)
    
    meta = fields.Nested(BagMeta, required=False)
    
    brand = fields.Nested(Brand, required=False)
    
    applied_promos = fields.List(fields.Dict(required=False), required=False)
    
    gst_details = fields.Nested(BagGSTDetails, required=False)
    
    b_id = fields.Int(required=False)
    
    current_status = fields.Nested(BagStatusHistory, required=False)
    
    bag_id = fields.Int(required=False)
    
    article = fields.Nested(Article, required=False)
    
    display_name = fields.Str(required=False)
    
    journey_type = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    affiliate_bag_details = fields.Nested(AffiliateBagDetails, required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
    payment_methods = fields.Dict(required=False)
    
    status = fields.Nested(BagReturnableCancelableStatus, required=False)
    
    bag_status = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    current_operational_status = fields.Nested(BagStatusHistory, required=False)
    
    dates = fields.Dict(required=False)
    

