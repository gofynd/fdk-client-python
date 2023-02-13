"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class QuestionSet(BaseSchema):
    # Orders swagger.json

    
    display_name = fields.Str(required=False)
    
    id = fields.Int(required=False)
    

