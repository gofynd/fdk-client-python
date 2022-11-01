"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .AppStore import AppStore



from .StoreDepartments import StoreDepartments



from .Page import Page



class ApplicationStoreListing(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(AppStore, required=False), required=False)
    
    filters = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
