"""Content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .FaqSchema import FaqSchema



class CreateFaqResponseSchema(BaseSchema):
    #  swagger.json

    
    faq = fields.Nested(FaqSchema, required=False)
    
