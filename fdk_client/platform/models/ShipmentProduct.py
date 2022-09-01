"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .FinancialBreakup import FinancialBreakup

from .Article import Article





from .Brand import Brand

from .BagStatusHistory import BagStatusHistory



from .Prices import Prices











from .BagStatusHistory import BagStatusHistory

from .BagStatusHistory import BagStatusHistory

from .BagMeta import BagMeta



from .BagReturnableCancelableStatus import BagReturnableCancelableStatus







from .AffiliateBagDetails import AffiliateBagDetails

from .Item import Item

from .BagGSTDetails import BagGSTDetails


class ShipmentProduct(BaseSchema):
    # Order swagger.json

    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    article = fields.Nested(Article, required=False)
    
    applied_promos = fields.List(fields.Dict(required=False), required=False)
    
    b_type = fields.Str(required=False)
    
    brand = fields.Nested(Brand, required=False)
    
    current_operational_status = fields.Nested(BagStatusHistory, required=False)
    
    payment_methods = fields.Dict(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    bag_id = fields.Int(required=False)
    
    entity_type = fields.Str(required=False)
    
    b_id = fields.Int(required=False)
    
    dates = fields.Dict(required=False)
    
    journey_type = fields.Str(required=False)
    
    current_status = fields.Nested(BagStatusHistory, required=False)
    
    bag_status = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    meta = fields.Nested(BagMeta, required=False)
    
    bag_update_time = fields.Float(required=False)
    
    status = fields.Nested(BagReturnableCancelableStatus, required=False)
    
    order_integration_id = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
    affiliate_bag_details = fields.Nested(AffiliateBagDetails, required=False)
    
    item = fields.Nested(Item, required=False)
    
    gst_details = fields.Nested(BagGSTDetails, required=False)
    

