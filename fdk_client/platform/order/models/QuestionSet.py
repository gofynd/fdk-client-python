"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class QuestionSet(BaseSchema):
    #  swagger.json

    
    display_name = fields.Str(required=False)
    
    id = fields.Int(required=False)
    