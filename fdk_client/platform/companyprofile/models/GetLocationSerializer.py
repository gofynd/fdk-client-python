"""companyprofile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .SellerPhoneNumber import SellerPhoneNumber









from .UserSerializer import UserSerializer





from .LocationManagerSerializer import LocationManagerSerializer















from .GetCompanySerializer import GetCompanySerializer



from .GetAddressSerializer import GetAddressSerializer



from .UserSerializer import UserSerializer



from .UserSerializer import UserSerializer



from .Document import Document



from .InvoiceDetailsSerializer import InvoiceDetailsSerializer



from .HolidaySchemaSerializer import HolidaySchemaSerializer



from .ProductReturnConfigSerializer import ProductReturnConfigSerializer







from .LocationDayWiseSerializer import LocationDayWiseSerializer



class GetLocationSerializer(BaseSchema):
    #  swagger.json

    
    stage = fields.Str(required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    store_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    warnings = fields.Dict(required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    verified_on = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    phone_number = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    company = fields.Nested(GetCompanySerializer, required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    holiday = fields.List(fields.Nested(HolidaySchemaSerializer, required=False), required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    modified_on = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
