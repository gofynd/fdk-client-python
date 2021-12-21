"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .CreateUpdateAddressSerializer import CreateUpdateAddressSerializer



















from .Document import Document

from .BusinessDetails import BusinessDetails

from .ContactDetails import ContactDetails


class UpdateCompany(BaseSchema):
    # CompanyProfile swagger.json

    
    addresses = fields.List(fields.Nested(CreateUpdateAddressSerializer, required=False), required=False)
    
    name = fields.Str(required=False)
    
    business_type = fields.Str(required=False)
    
    franchise_enabled = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    company_type = fields.Str(required=False)
    
    business_info = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    
    reject_reason = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    business_details = fields.Nested(BusinessDetails, required=False)
    
    contact_details = fields.Nested(ContactDetails, required=False)
    

