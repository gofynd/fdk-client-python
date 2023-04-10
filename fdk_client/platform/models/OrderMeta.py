"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .BillingStaffDetails import BillingStaffDetails





















from .TransactionData import TransactionData











from .PlatformUserDetails import PlatformUserDetails


class OrderMeta(BaseSchema):
    # Order swagger.json

    
    extra_meta = fields.Dict(required=False)
    
    billing_staff_details = fields.Nested(BillingStaffDetails, required=False)
    
    staff = fields.Dict(required=False)
    
    company_logo = fields.Str(required=False)
    
    ordering_store = fields.Int(required=False)
    
    comment = fields.Str(required=False)
    
    order_platform = fields.Str(required=False)
    
    order_child_entities = fields.List(fields.Str(required=False), required=False)
    
    order_type = fields.Str(required=False)
    
    files = fields.List(fields.Dict(required=False), required=False)
    
    cart_id = fields.Int(required=False)
    
    payment_type = fields.Str(required=False)
    
    transaction_data = fields.Nested(TransactionData, required=False)
    
    order_tags = fields.List(fields.Dict(required=False), required=False)
    
    mongo_cart_id = fields.Int(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    employee_id = fields.Int(required=False)
    
    customer_note = fields.Str(required=False)
    
    platform_user_details = fields.Nested(PlatformUserDetails, required=False)
    

