"""CompanyProfile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CompanySocialAccounts import CompanySocialAccounts





class CompanyDetails(BaseSchema):
    #  swagger.json

    
    socials = fields.List(fields.Nested(CompanySocialAccounts, required=False), required=False)
    
    website_url = fields.Str(required=False)
    
