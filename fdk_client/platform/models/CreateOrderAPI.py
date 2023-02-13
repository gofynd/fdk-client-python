"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PaymentInfo import PaymentInfo

from .TaxInfo import TaxInfo



from .Charge import Charge





from .Shipment import Shipment



from .ShippingInfo import ShippingInfo

from .BillingInfo import BillingInfo


class CreateOrderAPI(BaseSchema):
    # OrderManage swagger.json

    
    payment_info = fields.Nested(PaymentInfo, required=False)
    
    tax_info = fields.Nested(TaxInfo, required=False)
    
    external_creation_date = fields.Str(required=False)
    
    charges = fields.List(fields.Nested(Charge, required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    external_order_id = fields.Str(required=False)
    
    shipments = fields.List(fields.Nested(Shipment, required=False), required=False)
    
    currency_info = fields.Dict(required=False)
    
    shipping_info = fields.Nested(ShippingInfo, required=False)
    
    billing_info = fields.Nested(BillingInfo, required=False)
    

