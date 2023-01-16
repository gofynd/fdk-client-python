"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .PaymentInfo import PaymentInfo

from .Shipment import Shipment

from .BillingInfo import BillingInfo

from .TaxInfo import TaxInfo

from .ShippingInfo import ShippingInfo



from .Charge import Charge


class CreateOrderAPI(BaseSchema):
    # Order swagger.json

    
    external_creation_date = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    currency_info = fields.Dict(required=False)
    
    external_order_id = fields.Str(required=False)
    
    payment_info = fields.Nested(PaymentInfo, required=False)
    
    shipments = fields.List(fields.Nested(Shipment, required=False), required=False)
    
    billing_info = fields.Nested(BillingInfo, required=False)
    
    tax_info = fields.Nested(TaxInfo, required=False)
    
    shipping_info = fields.Nested(ShippingInfo, required=False)
    
    application_id = fields.Str(required=False)
    
    charges = fields.List(fields.Nested(Charge, required=False), required=False)
    

