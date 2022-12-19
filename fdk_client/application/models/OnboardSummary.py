"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class OnboardSummary(BaseSchema):
    # Payment swagger.json

    
    status = fields.Boolean(required=False)
    
    session = fields.Dict(required=False)
    
    redirect_url = fields.Str(required=False)
    

