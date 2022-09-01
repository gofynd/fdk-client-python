"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .LocationManagerSerializer import LocationManagerSerializer

from .LocationIntegrationType import LocationIntegrationType





from .ProductReturnConfigSerializer import ProductReturnConfigSerializer

from .BaseUserSerializer import BaseUserSerializer









from .InvoiceDetailsSerializer import InvoiceDetailsSerializer

from .BaseUserSerializer import BaseUserSerializer





from .LocationDayWiseSerializer import LocationDayWiseSerializer

from .GetCompanySerializer import GetCompanySerializer

from .Document import Document

from .BaseUserSerializer import BaseUserSerializer

from .SellerPhoneNumber import SellerPhoneNumber











from .GetAddressSerializer import GetAddressSerializer


class GetLocationSerializer(BaseSchema):
    # Catalog swagger.json

    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    integration_type = fields.Nested(LocationIntegrationType, required=False)
    
    modified_on = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    modified_by = fields.Nested(BaseUserSerializer, required=False)
    
    verified_on = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    warnings = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    verified_by = fields.Nested(BaseUserSerializer, required=False)
    
    stage = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    
    company = fields.Nested(GetCompanySerializer, required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    created_by = fields.Nested(BaseUserSerializer, required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    phone_number = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    

