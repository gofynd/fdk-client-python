"""Content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .SeoSchema import SeoSchema



class SeoComponent(BaseSchema):
    #  swagger.json

    
    seo = fields.Nested(SeoSchema, required=False)
    
