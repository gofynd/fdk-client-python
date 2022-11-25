"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Page import Page



from .CompanyBrandDetail import CompanyBrandDetail



class OptinCompanyBrandDetailsView(BaseSchema):
    #  swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(CompanyBrandDetail, required=False), required=False)
    
