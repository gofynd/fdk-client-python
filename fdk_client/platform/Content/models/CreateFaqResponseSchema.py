"""Content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .FaqSchema import FaqSchema



class CreateFaqResponseSchema(BaseSchema):
    #  swagger.json

    
    faq = fields.Nested(FaqSchema, required=False)
    
