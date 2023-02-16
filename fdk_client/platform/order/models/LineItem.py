"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .Charge import Charge







class LineItem(BaseSchema):
    #  swagger.json

    
    quantity = fields.Int(required=False)
    
    meta = fields.Dict(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    charges = fields.List(fields.Nested(Charge, required=False), required=False)
    
    external_line_id = fields.Str(required=False)
    
    custom_messasge = fields.Str(required=False)
    
