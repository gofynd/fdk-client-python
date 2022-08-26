"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .LocationDayWiseSerializer import LocationDayWiseSerializer

from .LocationIntegrationType import LocationIntegrationType

from .SellerPhoneNumber import SellerPhoneNumber



from .ProductReturnConfigSerializer import ProductReturnConfigSerializer

from .BaseUserSerializer import BaseUserSerializer

from .BaseUserSerializer import BaseUserSerializer



from .LocationManagerSerializer import LocationManagerSerializer





from .GetAddressSerializer import GetAddressSerializer

from .BaseUserSerializer import BaseUserSerializer











from .GetCompanySerializer import GetCompanySerializer







from .Document import Document



from .InvoiceDetailsSerializer import InvoiceDetailsSerializer


class GetLocationSerializer(BaseSchema):
    # Catalog swagger.json

    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    integration_type = fields.Nested(LocationIntegrationType, required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    created_by = fields.Nested(BaseUserSerializer, required=False)
    
    modified_by = fields.Nested(BaseUserSerializer, required=False)
    
    modified_on = fields.Str(required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    stage = fields.Str(required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    verified_by = fields.Nested(BaseUserSerializer, required=False)
    
    name = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    company = fields.Nested(GetCompanySerializer, required=False)
    
    phone_number = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    warnings = fields.Dict(required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    

