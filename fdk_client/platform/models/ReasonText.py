"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ReasonText(BaseSchema):
    # Order swagger.json

    
    text = fields.Str(required=False)
    
    id = fields.Int(required=False)
    

