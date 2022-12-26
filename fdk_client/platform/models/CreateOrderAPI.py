"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .Shipment import Shipment



from .PaymentInfo import PaymentInfo





from .BillingInfo import BillingInfo

from .TaxInfo import TaxInfo

from .Charge import Charge

from .ShippingInfo import ShippingInfo


class CreateOrderAPI(BaseSchema):
    # Order swagger.json

    
    external_order_id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    shipments = fields.List(fields.Nested(Shipment, required=False), required=False)
    
    external_creation_date = fields.Str(required=False)
    
    payment_info = fields.Nested(PaymentInfo, required=False)
    
    currency_info = fields.Dict(required=False)
    
    application_id = fields.Str(required=False)
    
    billing_info = fields.Nested(BillingInfo, required=False)
    
    tax_info = fields.Nested(TaxInfo, required=False)
    
    charges = fields.List(fields.Nested(Charge, required=False), required=False)
    
    shipping_info = fields.Nested(ShippingInfo, required=False)
    

