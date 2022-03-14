"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductReturnConfigSerializer import ProductReturnConfigSerializer

from .UserSerializer1 import UserSerializer1

from .UserSerializer1 import UserSerializer1

from .InvoiceDetailsSerializer import InvoiceDetailsSerializer









from .GetCompanySerializer import GetCompanySerializer

from .LocationIntegrationType import LocationIntegrationType









from .GetAddressSerializer import GetAddressSerializer





from .LocationManagerSerializer import LocationManagerSerializer

from .SellerPhoneNumber import SellerPhoneNumber

from .UserSerializer1 import UserSerializer1

from .LocationDayWiseSerializer import LocationDayWiseSerializer

from .Document import Document








class GetLocationSerializer(BaseSchema):
    # Catalog swagger.json

    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    verified_by = fields.Nested(UserSerializer1, required=False)
    
    created_by = fields.Nested(UserSerializer1, required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    store_type = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    company = fields.Nested(GetCompanySerializer, required=False)
    
    integration_type = fields.Nested(LocationIntegrationType, required=False)
    
    uid = fields.Int(required=False)
    
    modified_on = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    phone_number = fields.Str(required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    modified_by = fields.Nested(UserSerializer1, required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    

