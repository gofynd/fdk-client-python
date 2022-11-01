"""Configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ApplicationInfo import ApplicationInfo



from .CompanyInfo import CompanyInfo



from .OwnerInfo import OwnerInfo



class ApplicationAboutResponse(BaseSchema):
    #  swagger.json

    
    application_info = fields.Nested(ApplicationInfo, required=False)
    
    company_info = fields.Nested(CompanyInfo, required=False)
    
    owner_info = fields.Nested(OwnerInfo, required=False)
    
