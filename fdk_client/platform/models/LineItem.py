"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Charge import Charge










class LineItem(BaseSchema):
    # Order swagger.json

    
    external_line_id = fields.Str(required=False)
    
    charges = fields.List(fields.Nested(Charge, required=False), required=False)
    
    seller_identifier = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    custom_messasge = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    

