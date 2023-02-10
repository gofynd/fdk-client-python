"""companyprofile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .ContactDetails import ContactDetails



from .BusinessDetails import BusinessDetails







from .CreateUpdateAddressSerializer import CreateUpdateAddressSerializer









from .Document import Document





from .CompanyTaxesSerializer1 import CompanyTaxesSerializer1





class UpdateCompany(BaseSchema):
    #  swagger.json

    
    warnings = fields.Dict(required=False)
    
    franchise_enabled = fields.Boolean(required=False)
    
    contact_details = fields.Nested(ContactDetails, required=False)
    
    business_details = fields.Nested(BusinessDetails, required=False)
    
    business_type = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    addresses = fields.List(fields.Nested(CreateUpdateAddressSerializer, required=False), required=False)
    
    business_info = fields.Str(required=False)
    
    company_type = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    reject_reason = fields.Str(required=False)
    
    taxes = fields.List(fields.Nested(CompanyTaxesSerializer1, required=False), required=False)
    
    name = fields.Str(required=False)
    
