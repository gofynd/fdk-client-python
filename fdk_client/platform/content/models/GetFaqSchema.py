"""content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .FaqSchema import FaqSchema



class GetFaqSchema(BaseSchema):
    #  swagger.json

    
    faqs = fields.List(fields.Nested(FaqSchema, required=False), required=False)
    
