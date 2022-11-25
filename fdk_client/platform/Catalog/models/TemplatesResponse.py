"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Page import Page



from .ProductTemplate import ProductTemplate



class TemplatesResponse(BaseSchema):
    #  swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.Nested(ProductTemplate, required=False)
    
