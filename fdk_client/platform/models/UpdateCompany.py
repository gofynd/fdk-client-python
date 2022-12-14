"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .Document import Document



from .ContactDetails import ContactDetails





from .CreateUpdateAddressSerializer import CreateUpdateAddressSerializer





from .CompanyTaxesSerializer1 import CompanyTaxesSerializer1



from .BusinessDetails import BusinessDetails


class UpdateCompany(BaseSchema):
    # CompanyProfile swagger.json

    
    reject_reason = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    company_type = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    business_info = fields.Str(required=False)
    
    contact_details = fields.Nested(ContactDetails, required=False)
    
    warnings = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    addresses = fields.List(fields.Nested(CreateUpdateAddressSerializer, required=False), required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    business_type = fields.Str(required=False)
    
    taxes = fields.List(fields.Nested(CompanyTaxesSerializer1, required=False), required=False)
    
    franchise_enabled = fields.Boolean(required=False)
    
    business_details = fields.Nested(BusinessDetails, required=False)
    

