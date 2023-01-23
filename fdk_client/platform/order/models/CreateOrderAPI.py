"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .BillingInfo import BillingInfo





from .PaymentInfo import PaymentInfo



from .ShippingInfo import ShippingInfo





from .Charge import Charge





from .TaxInfo import TaxInfo



from .Shipment import Shipment



class CreateOrderAPI(BaseSchema):
    #  swagger.json

    
    external_order_id = fields.Str(required=False)
    
    billing_info = fields.Nested(BillingInfo, required=False)
    
    currency_info = fields.Dict(required=False)
    
    payment_info = fields.Nested(PaymentInfo, required=False)
    
    shipping_info = fields.Nested(ShippingInfo, required=False)
    
    external_creation_date = fields.Str(required=False)
    
    charges = fields.List(fields.Nested(Charge, required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    tax_info = fields.Nested(TaxInfo, required=False)
    
    shipments = fields.List(fields.Nested(Shipment, required=False), required=False)
    
