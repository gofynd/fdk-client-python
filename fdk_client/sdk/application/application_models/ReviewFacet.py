"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema












class ReviewFacet(BaseSchema):
    # Feedback swagger.json

    
    display = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    selected = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    type = fields.Str(required=False)
    

