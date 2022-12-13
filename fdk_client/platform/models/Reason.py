"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .QuestionSet import QuestionSet


class Reason(BaseSchema):
    # Order swagger.json

    
    qc_type = fields.List(fields.Str(required=False), required=False)
    
    id = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    
    question_set = fields.List(fields.Nested(QuestionSet, required=False), required=False)
    

