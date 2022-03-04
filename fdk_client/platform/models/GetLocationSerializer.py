"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .UserSerializer1 import UserSerializer1











from .GetAddressSerializer import GetAddressSerializer





from .LocationManagerSerializer import LocationManagerSerializer



from .UserSerializer1 import UserSerializer1



from .InvoiceDetailsSerializer import InvoiceDetailsSerializer

from .SellerPhoneNumber import SellerPhoneNumber

from .GetCompanySerializer import GetCompanySerializer





from .LocationIntegrationType import LocationIntegrationType



from .ProductReturnConfigSerializer import ProductReturnConfigSerializer

from .UserSerializer1 import UserSerializer1



from .Document import Document

from .LocationDayWiseSerializer import LocationDayWiseSerializer


class GetLocationSerializer(BaseSchema):
    # Catalog swagger.json

    
    verified_by = fields.Nested(UserSerializer1, required=False)
    
    modified_on = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    
    code = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    stage = fields.Str(required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    phone_number = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    verified_on = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer1, required=False)
    
    created_on = fields.Str(required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    company = fields.Nested(GetCompanySerializer, required=False)
    
    name = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    integration_type = fields.Nested(LocationIntegrationType, required=False)
    
    uid = fields.Int(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    created_by = fields.Nested(UserSerializer1, required=False)
    
    display_name = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    

