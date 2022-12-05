"""companyprofile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .InvoiceDetailsSerializer import InvoiceDetailsSerializer









from .UserSerializer import UserSerializer



from .SellerPhoneNumber import SellerPhoneNumber



from .UserSerializer import UserSerializer









from .GetCompanySerializer import GetCompanySerializer



from .LocationDayWiseSerializer import LocationDayWiseSerializer









from .Document import Document



from .ProductReturnConfigSerializer import ProductReturnConfigSerializer





from .GetAddressSerializer import GetAddressSerializer





from .UserSerializer import UserSerializer





from .LocationManagerSerializer import LocationManagerSerializer



class GetLocationSerializer(BaseSchema):
    #  swagger.json

    
    phone_number = fields.Str(required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    verified_on = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    uid = fields.Int(required=False)
    
    created_on = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    
    company = fields.Nested(GetCompanySerializer, required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    stage = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    modified_on = fields.Str(required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
