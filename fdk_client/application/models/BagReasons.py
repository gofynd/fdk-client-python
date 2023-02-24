"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .BagReasonMeta import BagReasonMeta







from .QuestionSet import QuestionSet




class BagReasons(BaseSchema):
    # Order swagger.json

    
    meta = fields.Nested(BagReasonMeta, required=False)
    
    qc_type = fields.List(fields.Str(required=False), required=False)
    
    display_name = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    question_set = fields.List(fields.Nested(QuestionSet, required=False), required=False)
    
    reasons = fields.List(fields.Nested(lambda: BagReasons(exclude=('reasons')), required=False), required=False)
    

