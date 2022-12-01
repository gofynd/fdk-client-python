"""rma Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class QuestionSet(BaseSchema):
    #  swagger.json

    
    id = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    
