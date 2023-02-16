"""content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .CustomPageSchema import CustomPageSchema



class CustomPage(BaseSchema):
    #  swagger.json

    
    data = fields.Nested(CustomPageSchema, required=False)
    
