"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class FeedbackForm(BaseSchema):
    # Lead swagger.json

    
    inputs = fields.Dict(required=False)
    
    title = fields.Str(required=False)
    
    timestamps = fields.Dict(required=False)
    

