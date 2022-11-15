"""CompanyProfile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CompanyBrandSerializer import CompanyBrandSerializer



from .Page import Page



class CompanyBrandListSerializer(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(CompanyBrandSerializer, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
