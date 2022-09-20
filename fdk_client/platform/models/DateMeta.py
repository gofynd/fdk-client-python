"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class DateMeta(BaseSchema):
    # Feedback swagger.json

    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    

