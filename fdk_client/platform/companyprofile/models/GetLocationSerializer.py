"""companyprofile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .UserSerializer import UserSerializer





from .GetAddressSerializer import GetAddressSerializer



from .InvoiceDetailsSerializer import InvoiceDetailsSerializer





from .LocationDayWiseSerializer import LocationDayWiseSerializer





from .GetCompanySerializer import GetCompanySerializer



from .UserSerializer import UserSerializer



from .SellerPhoneNumber import SellerPhoneNumber





from .ProductReturnConfigSerializer import ProductReturnConfigSerializer







from .LocationManagerSerializer import LocationManagerSerializer







from .HolidaySchemaSerializer import HolidaySchemaSerializer







from .Document import Document



from .UserSerializer import UserSerializer



class GetLocationSerializer(BaseSchema):
    #  swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    display_name = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    verified_on = fields.Str(required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    store_type = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    code = fields.Str(required=False)
    
    company = fields.Nested(GetCompanySerializer, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    created_on = fields.Str(required=False)
    
    phone_number = fields.Str(required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    holiday = fields.List(fields.Nested(HolidaySchemaSerializer, required=False), required=False)
    
    warnings = fields.Dict(required=False)
    
    stage = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
