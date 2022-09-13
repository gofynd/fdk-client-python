"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .Article import Article

from .BagStatusHistory import BagStatusHistory

from .BagMeta import BagMeta





from .AffiliateBagDetails import AffiliateBagDetails



from .Brand import Brand

from .Item import Item

from .Prices import Prices



from .FinancialBreakup import FinancialBreakup









from .BagGSTDetails import BagGSTDetails





from .BagStatusHistory import BagStatusHistory

from .BagReturnableCancelableStatus import BagReturnableCancelableStatus

from .BagStatusHistory import BagStatusHistory


class ShipmentProduct(BaseSchema):
    # Order swagger.json

    
    payment_methods = fields.Dict(required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
    article = fields.Nested(Article, required=False)
    
    current_operational_status = fields.Nested(BagStatusHistory, required=False)
    
    meta = fields.Nested(BagMeta, required=False)
    
    bag_update_time = fields.Float(required=False)
    
    bag_id = fields.Int(required=False)
    
    affiliate_bag_details = fields.Nested(AffiliateBagDetails, required=False)
    
    applied_promos = fields.List(fields.Dict(required=False), required=False)
    
    brand = fields.Nested(Brand, required=False)
    
    item = fields.Nested(Item, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    journey_type = fields.Str(required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    b_id = fields.Int(required=False)
    
    dates = fields.Dict(required=False)
    
    order_integration_id = fields.Str(required=False)
    
    b_type = fields.Str(required=False)
    
    gst_details = fields.Nested(BagGSTDetails, required=False)
    
    display_name = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    current_status = fields.Nested(BagStatusHistory, required=False)
    
    status = fields.Nested(BagReturnableCancelableStatus, required=False)
    
    bag_status = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    

