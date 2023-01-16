"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Page import Page



from .ApplicationDepartment import ApplicationDepartment



class ApplicationDepartmentListingResponse(BaseSchema):
    #  swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(ApplicationDepartment, required=False), required=False)
    
