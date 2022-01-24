"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .InvoiceDetailsSerializer import InvoiceDetailsSerializer





from .LocationIntegrationType import LocationIntegrationType









from .GetAddressSerializer import GetAddressSerializer







from .UserSerializer1 import UserSerializer1

from .UserSerializer1 import UserSerializer1

from .UserSerializer1 import UserSerializer1



from .Document import Document

from .ProductReturnConfigSerializer import ProductReturnConfigSerializer

from .LocationDayWiseSerializer import LocationDayWiseSerializer



from .GetCompanySerializer import GetCompanySerializer

from .LocationManagerSerializer import LocationManagerSerializer

from .SellerPhoneNumber import SellerPhoneNumber






class GetLocationSerializer(BaseSchema):
    # Catalog swagger.json

    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    display_name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    integration_type = fields.Nested(LocationIntegrationType, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    phone_number = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    name = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    
    modified_on = fields.Str(required=False)
    
    verified_by = fields.Nested(UserSerializer1, required=False)
    
    modified_by = fields.Nested(UserSerializer1, required=False)
    
    created_by = fields.Nested(UserSerializer1, required=False)
    
    stage = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    company = fields.Nested(GetCompanySerializer, required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    

