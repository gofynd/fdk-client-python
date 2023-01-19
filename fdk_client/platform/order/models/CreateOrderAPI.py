"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ShippingInfo import ShippingInfo





from .PaymentInfo import PaymentInfo





from .Shipment import Shipment







from .TaxInfo import TaxInfo



from .Charge import Charge



from .BillingInfo import BillingInfo



class CreateOrderAPI(BaseSchema):
    #  swagger.json

    
    shipping_info = fields.Nested(ShippingInfo, required=False)
    
    meta = fields.Dict(required=False)
    
    payment_info = fields.Nested(PaymentInfo, required=False)
    
    currency_info = fields.Dict(required=False)
    
    shipments = fields.List(fields.Nested(Shipment, required=False), required=False)
    
    external_order_id = fields.Str(required=False)
    
    external_creation_date = fields.Str(required=False)
    
    tax_info = fields.Nested(TaxInfo, required=False)
    
    charges = fields.List(fields.Nested(Charge, required=False), required=False)
    
    billing_info = fields.Nested(BillingInfo, required=False)
    
