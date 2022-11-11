"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CompanyBrandDetail import CompanyBrandDetail



from .Page import Page



class OptinCompanyBrandDetailsView(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(CompanyBrandDetail, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
