"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Page import Page



from .StoreDepartments import StoreDepartments



from .AppStore import AppStore



class ApplicationStoreListing(BaseSchema):
    #  swagger.json

    
    page = fields.Nested(Page, required=False)
    
    filters = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    
    items = fields.List(fields.Nested(AppStore, required=False), required=False)
    
