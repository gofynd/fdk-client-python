"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class WebRedirect(BaseSchema):

    
    link = fields.Str(required=False)
    
    type = fields.Str(required=False)
    

