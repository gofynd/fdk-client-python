"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Item import Item



from .BagMeta import BagMeta















from .BagReturnableCancelableStatus import BagReturnableCancelableStatus

from .BagGSTDetails import BagGSTDetails



from .BagStatusHistory import BagStatusHistory

from .AffiliateBagDetails import AffiliateBagDetails



from .BagStatusHistory import BagStatusHistory

from .Prices import Prices

from .Brand import Brand

from .Article import Article

from .FinancialBreakup import FinancialBreakup





from .BagStatusHistory import BagStatusHistory


class Bag(BaseSchema):
    # Order swagger.json

    
    item = fields.Nested(Item, required=False)
    
    entity_type = fields.Str(required=False)
    
    meta = fields.Nested(BagMeta, required=False)
    
    journey_type = fields.Str(required=False)
    
    b_id = fields.Int(required=False)
    
    dates = fields.Dict(required=False)
    
    display_name = fields.Str(required=False)
    
    applied_promos = fields.List(fields.Dict(required=False), required=False)
    
    bag_id = fields.Int(required=False)
    
    b_type = fields.Str(required=False)
    
    status = fields.Nested(BagReturnableCancelableStatus, required=False)
    
    gst_details = fields.Nested(BagGSTDetails, required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
    current_operational_status = fields.Nested(BagStatusHistory, required=False)
    
    affiliate_bag_details = fields.Nested(AffiliateBagDetails, required=False)
    
    bag_update_time = fields.Float(required=False)
    
    current_status = fields.Nested(BagStatusHistory, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    brand = fields.Nested(Brand, required=False)
    
    article = fields.Nested(Article, required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    order_integration_id = fields.Str(required=False)
    
    payment_methods = fields.Dict(required=False)
    
    bag_status = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    

