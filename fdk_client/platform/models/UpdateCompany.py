"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .Document import Document



from .BusinessDetails import BusinessDetails

from .ContactDetails import ContactDetails

from .CreateUpdateAddressSerializer import CreateUpdateAddressSerializer








class UpdateCompany(BaseSchema):
    # CompanyProfile swagger.json

    
    business_info = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    website_url = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    about_business = fields.Str(required=False)
    
    business_details = fields.Nested(BusinessDetails, required=False)
    
    contact_details = fields.Nested(ContactDetails, required=False)
    
    addresses = fields.List(fields.Nested(CreateUpdateAddressSerializer, required=False), required=False)
    
    store_name = fields.Str(required=False)
    
    company_type = fields.Str(required=False)
    
    annual_turnover = fields.Str(required=False)
    

