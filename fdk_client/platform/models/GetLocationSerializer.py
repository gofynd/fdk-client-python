"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .UserSerializer1 import UserSerializer1



from .LocationManagerSerializer import LocationManagerSerializer

from .UserSerializer1 import UserSerializer1

from .ProductReturnConfigSerializer import ProductReturnConfigSerializer

from .GetAddressSerializer import GetAddressSerializer





from .LocationIntegrationType import LocationIntegrationType



from .InvoiceDetailsSerializer import InvoiceDetailsSerializer





from .SellerPhoneNumber import SellerPhoneNumber



from .Document import Document



from .UserSerializer1 import UserSerializer1



from .LocationDayWiseSerializer import LocationDayWiseSerializer



from .GetCompanySerializer import GetCompanySerializer






class GetLocationSerializer(BaseSchema):
    # Catalog swagger.json

    
    stage = fields.Str(required=False)
    
    verified_by = fields.Nested(UserSerializer1, required=False)
    
    name = fields.Str(required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    created_by = fields.Nested(UserSerializer1, required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    display_name = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    integration_type = fields.Nested(LocationIntegrationType, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    uid = fields.Int(required=False)
    
    warnings = fields.Dict(required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    code = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer1, required=False)
    
    store_type = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    phone_number = fields.Str(required=False)
    
    company = fields.Nested(GetCompanySerializer, required=False)
    
    verified_on = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    

