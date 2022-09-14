"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .BusinessDetails import BusinessDetails



















from .CreateUpdateAddressSerializer import CreateUpdateAddressSerializer

from .Document import Document

from .CompanyTaxesSerializer import CompanyTaxesSerializer

from .ContactDetails import ContactDetails




class UpdateCompany(BaseSchema):
    # CompanyProfile swagger.json

    
    reject_reason = fields.Str(required=False)
    
    business_type = fields.Str(required=False)
    
    store_name = fields.Str(required=False)
    
    composite_taxation = fields.Str(required=False)
    
    business_info = fields.Str(required=False)
    
    business_details = fields.Nested(BusinessDetails, required=False)
    
    company_type = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    franchise_enabled = fields.Boolean(required=False)
    
    annual_turnover = fields.Str(required=False)
    
    website_url = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    about_business = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    addresses = fields.List(fields.Nested(CreateUpdateAddressSerializer, required=False), required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    taxes = fields.List(fields.Nested(CompanyTaxesSerializer, required=False), required=False)
    
    contact_details = fields.Nested(ContactDetails, required=False)
    
    _custom_json = fields.Dict(required=False)
    

