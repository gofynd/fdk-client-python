"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class OrderStatuses(BaseSchema):
    # Order swagger.json

    
    value = fields.Int(required=False)
    
    is_selected = fields.Boolean(required=False)
    
    display = fields.Str(required=False)
    

