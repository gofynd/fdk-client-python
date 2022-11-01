"""Content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .FAQ import FAQ



class CreateFaqSchema(BaseSchema):
    #  swagger.json

    
    faq = fields.Nested(FAQ, required=False)
    
