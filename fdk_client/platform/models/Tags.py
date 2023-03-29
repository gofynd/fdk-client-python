"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class Tags(BaseSchema):
    # Cart swagger.json

    
    tags = fields.Dict(required=False)
    

