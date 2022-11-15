"""CompanyProfile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .SellerPhoneNumber import SellerPhoneNumber





from .InvoiceDetailsSerializer import InvoiceDetailsSerializer







from .GetCompanySerializer import GetCompanySerializer





from .UserSerializer import UserSerializer





from .Document import Document







from .GetAddressSerializer import GetAddressSerializer













from .UserSerializer import UserSerializer



from .LocationDayWiseSerializer import LocationDayWiseSerializer



from .UserSerializer import UserSerializer





from .ProductReturnConfigSerializer import ProductReturnConfigSerializer



from .LocationManagerSerializer import LocationManagerSerializer



class GetLocationSerializer(BaseSchema):
    #  swagger.json

    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    phone_number = fields.Str(required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    code = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    company = fields.Nested(GetCompanySerializer, required=False)
    
    warnings = fields.Dict(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    uid = fields.Int(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    name = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    store_type = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    stage = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    modified_on = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    display_name = fields.Str(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
