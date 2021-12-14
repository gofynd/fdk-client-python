"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema



from .UIIcon import UIIcon






class UI(BaseSchema):
    # Feedback swagger.json

    
    feedback_question = fields.List(fields.Str(required=False), required=False)
    
    icon = fields.Nested(UIIcon, required=False)
    
    text = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    

