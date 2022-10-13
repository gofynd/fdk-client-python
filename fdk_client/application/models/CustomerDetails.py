"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class CustomerDetails(BaseSchema):
    # Cart swagger.json

    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    

