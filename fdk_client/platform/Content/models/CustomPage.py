"""Content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CustomPageSchema import CustomPageSchema



class CustomPage(BaseSchema):
    #  swagger.json

    
    data = fields.Nested(CustomPageSchema, required=False)
    
