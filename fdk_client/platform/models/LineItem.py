"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Charge import Charge












class LineItem(BaseSchema):
    # Order swagger.json

    
    charges = fields.List(fields.Nested(Charge, required=False), required=False)
    
    quantity = fields.Int(required=False)
    
    meta = fields.Dict(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    custom_messasge = fields.Str(required=False)
    
    external_line_id = fields.Str(required=False)
    

