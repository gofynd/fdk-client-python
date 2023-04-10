"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .ContactDetails import ContactDetails


class CompanyDetails(BaseSchema):
    # Order swagger.json

    
    company_gst = fields.Str(required=False)
    
    address = fields.Dict(required=False)
    
    company_id = fields.Int(required=False)
    
    company_cin = fields.Str(required=False)
    
    company_name = fields.Str(required=False)
    
    company_contact = fields.Nested(ContactDetails, required=False)
    

