"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Application import Application



from .Page import Page



class ApplicationsResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(Application, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
