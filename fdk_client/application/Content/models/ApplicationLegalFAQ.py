"""Content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class ApplicationLegalFAQ(BaseSchema):
    #  swagger.json

    
    question = fields.Str(required=False)
    
    answer = fields.Str(required=False)
    
