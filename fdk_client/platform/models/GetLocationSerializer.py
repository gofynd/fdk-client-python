"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .UserSerializer1 import UserSerializer1









from .SellerPhoneNumber import SellerPhoneNumber







from .UserSerializer1 import UserSerializer1

from .LocationIntegrationType import LocationIntegrationType

from .LocationDayWiseSerializer import LocationDayWiseSerializer

from .LocationManagerSerializer import LocationManagerSerializer



from .UserSerializer1 import UserSerializer1

from .GetCompanySerializer import GetCompanySerializer



from .ProductReturnConfigSerializer import ProductReturnConfigSerializer



from .Document import Document



from .GetAddressSerializer import GetAddressSerializer

from .InvoiceDetailsSerializer import InvoiceDetailsSerializer




class GetLocationSerializer(BaseSchema):
    # Catalog swagger.json

    
    modified_on = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer1, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    display_name = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    code = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer1, required=False)
    
    integration_type = fields.Nested(LocationIntegrationType, required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    name = fields.Str(required=False)
    
    verified_by = fields.Nested(UserSerializer1, required=False)
    
    company = fields.Nested(GetCompanySerializer, required=False)
    
    warnings = fields.Dict(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    verified_on = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    phone_number = fields.Str(required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    uid = fields.Int(required=False)
    

