"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .AppInventoryCompanies import AppInventoryCompanies



from .Page import Page



class CompaniesResponse(BaseSchema):
    #  swagger.json

    
    items = fields.Nested(AppInventoryCompanies, required=False)
    
    page = fields.Nested(Page, required=False)
    
