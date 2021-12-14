"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class DateMeta(BaseSchema):
    # Content swagger.json

    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    

