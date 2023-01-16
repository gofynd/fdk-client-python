"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .PaymentInfo import PaymentInfo





from .BillingInfo import BillingInfo





from .Shipment import Shipment



from .TaxInfo import TaxInfo



from .Charge import Charge



from .ShippingInfo import ShippingInfo







class CreateOrderAPI(BaseSchema):
    #  swagger.json

    
    payment_info = fields.Nested(PaymentInfo, required=False)
    
    currency_info = fields.Dict(required=False)
    
    billing_info = fields.Nested(BillingInfo, required=False)
    
    external_order_id = fields.Str(required=False)
    
    shipments = fields.List(fields.Nested(Shipment, required=False), required=False)
    
    tax_info = fields.Nested(TaxInfo, required=False)
    
    charges = fields.List(fields.Nested(Charge, required=False), required=False)
    
    shipping_info = fields.Nested(ShippingInfo, required=False)
    
    external_creation_date = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
