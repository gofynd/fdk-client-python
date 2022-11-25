"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .QuestionSet import QuestionSet









class BagReasons1(BaseSchema):
    #  swagger.json

    
    question_set = fields.List(fields.Nested(QuestionSet, required=False), required=False)
    
    id = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    
    qc_type = fields.List(fields.Str(required=False), required=False)
    
