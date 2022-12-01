"""content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .FaqSchema import FaqSchema



class FaqResponseSchema(BaseSchema):
    #  swagger.json

    
    faqs = fields.List(fields.Nested(FaqSchema, required=False), required=False)
    
