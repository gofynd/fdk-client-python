"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Document import Document







from .LocationDayWiseSerializer import LocationDayWiseSerializer

from .BaseUserSerializer import BaseUserSerializer



from .LocationManagerSerializer import LocationManagerSerializer





from .GetAddressSerializer import GetAddressSerializer

from .GetCompanySerializer import GetCompanySerializer

from .ProductReturnConfigSerializer import ProductReturnConfigSerializer







from .LocationIntegrationType import LocationIntegrationType

from .BaseUserSerializer import BaseUserSerializer



from .InvoiceDetailsSerializer import InvoiceDetailsSerializer

from .SellerPhoneNumber import SellerPhoneNumber





from .BaseUserSerializer import BaseUserSerializer


class GetLocationSerializer(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    code = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    created_by = fields.Nested(BaseUserSerializer, required=False)
    
    modified_on = fields.Str(required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    verified_on = fields.Str(required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    company = fields.Nested(GetCompanySerializer, required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    warnings = fields.Dict(required=False)
    
    phone_number = fields.Str(required=False)
    
    integration_type = fields.Nested(LocationIntegrationType, required=False)
    
    modified_by = fields.Nested(BaseUserSerializer, required=False)
    
    store_type = fields.Str(required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    display_name = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    verified_by = fields.Nested(BaseUserSerializer, required=False)
    

