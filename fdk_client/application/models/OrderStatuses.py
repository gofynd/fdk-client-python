"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class OrderStatuses(BaseSchema):
    # Order swagger.json

    
    is_selected = fields.Boolean(required=False)
    
    value = fields.Int(required=False)
    
    display = fields.Str(required=False)
    

