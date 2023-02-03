"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .BagReasonMeta import BagReasonMeta







from .QuestionSet import QuestionSet





class BagReasons(BaseSchema):
    #  swagger.json

    
    id = fields.Int(required=False)
    
    meta = fields.Nested(BagReasonMeta, required=False)
    
    display_name = fields.Str(required=False)
    
    reasons = fields.List(fields.Nested(lambda: BagReasons(exclude=('reasons')), required=False), required=False)
    
    question_set = fields.List(fields.Nested(QuestionSet, required=False), required=False)
    
    qc_type = fields.List(fields.Str(required=False), required=False)
    
