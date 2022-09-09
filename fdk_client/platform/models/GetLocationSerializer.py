"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .LocationDayWiseSerializer import LocationDayWiseSerializer





from .BaseUserSerializer import BaseUserSerializer

from .ProductReturnConfigSerializer import ProductReturnConfigSerializer

from .LocationIntegrationType import LocationIntegrationType



from .InvoiceDetailsSerializer import InvoiceDetailsSerializer



from .BaseUserSerializer import BaseUserSerializer









from .BaseUserSerializer import BaseUserSerializer

from .GetCompanySerializer import GetCompanySerializer

from .LocationManagerSerializer import LocationManagerSerializer







from .GetAddressSerializer import GetAddressSerializer

from .SellerPhoneNumber import SellerPhoneNumber



from .Document import Document


class GetLocationSerializer(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    warnings = fields.Dict(required=False)
    
    display_name = fields.Str(required=False)
    
    modified_by = fields.Nested(BaseUserSerializer, required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    integration_type = fields.Nested(LocationIntegrationType, required=False)
    
    uid = fields.Int(required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    store_type = fields.Str(required=False)
    
    verified_by = fields.Nested(BaseUserSerializer, required=False)
    
    stage = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    code = fields.Str(required=False)
    
    created_by = fields.Nested(BaseUserSerializer, required=False)
    
    company = fields.Nested(GetCompanySerializer, required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    phone_number = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    

