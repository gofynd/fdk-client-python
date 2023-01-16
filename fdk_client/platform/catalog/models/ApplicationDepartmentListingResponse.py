"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ApplicationDepartment import ApplicationDepartment



from .Page import Page



class ApplicationDepartmentListingResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(ApplicationDepartment, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
