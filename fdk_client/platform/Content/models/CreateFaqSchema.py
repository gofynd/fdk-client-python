"""Content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .FAQ import FAQ



class CreateFaqSchema(BaseSchema):
    #  swagger.json

    
    faq = fields.Nested(FAQ, required=False)
    
