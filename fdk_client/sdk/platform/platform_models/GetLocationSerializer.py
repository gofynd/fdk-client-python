"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema









from .GetCompanySerializer import GetCompanySerializer

from .ProductReturnConfigSerializer import ProductReturnConfigSerializer

from .UserSerializer1 import UserSerializer1

from .LocationIntegrationType import LocationIntegrationType

from .UserSerializer1 import UserSerializer1

from .UserSerializer1 import UserSerializer1



from .LocationDayWiseSerializer import LocationDayWiseSerializer



from .SellerPhoneNumber import SellerPhoneNumber

from .LocationManagerSerializer import LocationManagerSerializer



from .Document import Document



from .InvoiceDetailsSerializer import InvoiceDetailsSerializer

from .GetAddressSerializer import GetAddressSerializer












class GetLocationSerializer(BaseSchema):

    
    modified_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    company = fields.Nested(GetCompanySerializer, required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    verified_by = fields.Nested(UserSerializer1, required=False)
    
    integration_type = fields.Nested(LocationIntegrationType, required=False)
    
    created_by = fields.Nested(UserSerializer1, required=False)
    
    modified_by = fields.Nested(UserSerializer1, required=False)
    
    store_type = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    display_name = fields.Str(required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    verified_on = fields.Str(required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    stage = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    
    phone_number = fields.Str(required=False)
    
    code = fields.Str(required=False)
    

