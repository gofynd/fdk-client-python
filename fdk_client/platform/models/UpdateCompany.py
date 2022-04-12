"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .ContactDetails import ContactDetails



from .BusinessDetails import BusinessDetails

from .Document import Document





from .CompanyTax import CompanyTax



from .CreateUpdateAddressSerializer import CreateUpdateAddressSerializer


class UpdateCompany(BaseSchema):
    # CompanyProfile swagger.json

    
    reject_reason = fields.Str(required=False)
    
    franchise_enabled = fields.Boolean(required=False)
    
    company_type = fields.Str(required=False)
    
    business_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    contact_details = fields.Nested(ContactDetails, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    business_details = fields.Nested(BusinessDetails, required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    warnings = fields.Dict(required=False)
    
    business_info = fields.Str(required=False)
    
    taxes = fields.List(fields.Nested(CompanyTax, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    addresses = fields.List(fields.Nested(CreateUpdateAddressSerializer, required=False), required=False)
    

