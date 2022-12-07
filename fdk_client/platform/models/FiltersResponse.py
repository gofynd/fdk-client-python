"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class FiltersResponse(BaseSchema):
    # Orders swagger.json

    
    advance = fields.List(fields.Dict(required=False), required=False)
    

