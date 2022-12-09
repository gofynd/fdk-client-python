"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .Shipment import Shipment

from .Charge import Charge



from .ShippingInfo import ShippingInfo

from .PaymentInfo import PaymentInfo



from .BillingInfo import BillingInfo

from .TaxInfo import TaxInfo




class CreateOrderAPI(BaseSchema):
    # OrderManage swagger.json

    
    application_id = fields.Str(required=False)
    
    currency_info = fields.Dict(required=False)
    
    shipments = fields.List(fields.Nested(Shipment, required=False), required=False)
    
    charges = fields.List(fields.Nested(Charge, required=False), required=False)
    
    external_creation_date = fields.Str(required=False)
    
    shipping_info = fields.Nested(ShippingInfo, required=False)
    
    payment_info = fields.Nested(PaymentInfo, required=False)
    
    meta = fields.Dict(required=False)
    
    billing_info = fields.Nested(BillingInfo, required=False)
    
    tax_info = fields.Nested(TaxInfo, required=False)
    
    external_order_id = fields.Str(required=False)
    

