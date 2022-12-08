"""companyprofile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .LocationDayWiseSerializer import LocationDayWiseSerializer





from .InvoiceDetailsSerializer import InvoiceDetailsSerializer









from .SellerPhoneNumber import SellerPhoneNumber





from .Document import Document





from .LocationManagerSerializer import LocationManagerSerializer



from .ProductReturnConfigSerializer import ProductReturnConfigSerializer





from .GetAddressSerializer import GetAddressSerializer







class LocationSerializer(BaseSchema):
    #  swagger.json

    
    company = fields.Int(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    store_type = fields.Str(required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    stage = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    display_name = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    warnings = fields.Dict(required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    name = fields.Str(required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    uid = fields.Int(required=False)
    
    code = fields.Str(required=False)
    
