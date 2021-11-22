"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *



from .ContactDetails import ContactDetails



from .Document import Document



from .CreateUpdateAddressSerializer import CreateUpdateAddressSerializer

from .BusinessDetails import BusinessDetails












class UpdateCompany(Schema):

    
    name = fields.Str(required=False)
    
    contact_details = fields.Nested(ContactDetails, required=False)
    
    warnings = fields.Dict(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    addresses = fields.List(fields.Nested(CreateUpdateAddressSerializer, required=False), required=False)
    
    business_details = fields.Nested(BusinessDetails, required=False)
    
    business_type = fields.Str(required=False)
    
    company_type = fields.Str(required=False)
    
    franchise_enabled = fields.Boolean(required=False)
    
    business_info = fields.Str(required=False)
    
    reject_reason = fields.Str(required=False)
    

