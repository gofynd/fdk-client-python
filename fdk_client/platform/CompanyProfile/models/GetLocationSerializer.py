"""CompanyProfile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .LocationDayWiseSerializer import LocationDayWiseSerializer





from .UserSerializer import UserSerializer





from .UserSerializer import UserSerializer









from .GetAddressSerializer import GetAddressSerializer



from .GetCompanySerializer import GetCompanySerializer





from .LocationManagerSerializer import LocationManagerSerializer









from .InvoiceDetailsSerializer import InvoiceDetailsSerializer



from .SellerPhoneNumber import SellerPhoneNumber





from .LocationIntegrationType import LocationIntegrationType



from .Document import Document



from .ProductReturnConfigSerializer import ProductReturnConfigSerializer



from .UserSerializer import UserSerializer



class GetLocationSerializer(BaseSchema):
    #  swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    phone_number = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    store_type = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    code = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    company = fields.Nested(GetCompanySerializer, required=False)
    
    modified_on = fields.Str(required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    warnings = fields.Dict(required=False)
    
    verified_on = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    display_name = fields.Str(required=False)
    
    integration_type = fields.Nested(LocationIntegrationType, required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
