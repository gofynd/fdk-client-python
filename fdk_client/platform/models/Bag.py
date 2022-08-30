"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .BagStatusHistory import BagStatusHistory

from .AffiliateBagDetails import AffiliateBagDetails

from .BagReturnableCancelableStatus import BagReturnableCancelableStatus







from .Prices import Prices

from .BagStatusHistory import BagStatusHistory









from .BagMeta import BagMeta

from .Item import Item

from .FinancialBreakup import FinancialBreakup





from .Brand import Brand



from .BagStatusHistory import BagStatusHistory

from .Article import Article



from .BagGSTDetails import BagGSTDetails




class Bag(BaseSchema):
    # Order swagger.json

    
    current_operational_status = fields.Nested(BagStatusHistory, required=False)
    
    affiliate_bag_details = fields.Nested(AffiliateBagDetails, required=False)
    
    status = fields.Nested(BagReturnableCancelableStatus, required=False)
    
    b_id = fields.Int(required=False)
    
    payment_methods = fields.Dict(required=False)
    
    b_type = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    current_status = fields.Nested(BagStatusHistory, required=False)
    
    applied_promos = fields.List(fields.Dict(required=False), required=False)
    
    order_integration_id = fields.Str(required=False)
    
    journey_type = fields.Str(required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
    meta = fields.Nested(BagMeta, required=False)
    
    item = fields.Nested(Item, required=False)
    
    financial_breakup = fields.List(fields.Nested(FinancialBreakup, required=False), required=False)
    
    bag_id = fields.Int(required=False)
    
    bag_update_time = fields.Float(required=False)
    
    brand = fields.Nested(Brand, required=False)
    
    display_name = fields.Str(required=False)
    
    bag_status = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    article = fields.Nested(Article, required=False)
    
    dates = fields.Dict(required=False)
    
    gst_details = fields.Nested(BagGSTDetails, required=False)
    
    entity_type = fields.Str(required=False)
    

