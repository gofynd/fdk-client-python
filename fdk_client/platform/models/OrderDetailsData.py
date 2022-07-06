"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class OrderDetailsData(BaseSchema):
    # Orders swagger.json

    
    data = fields.Str(required=False)
    

