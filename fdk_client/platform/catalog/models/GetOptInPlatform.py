"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CompanyOptIn import CompanyOptIn



from .Page import Page



class GetOptInPlatform(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(CompanyOptIn, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
