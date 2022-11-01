"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Category import Category



from .Page import Page



class CategoryResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(Category, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
