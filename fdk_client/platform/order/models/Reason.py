"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .QuestionSet import QuestionSet









class Reason(BaseSchema):
    #  swagger.json

    
    question_set = fields.List(fields.Nested(QuestionSet, required=False), required=False)
    
    id = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    
    qc_type = fields.List(fields.Str(required=False), required=False)
    
