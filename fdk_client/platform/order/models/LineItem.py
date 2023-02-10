"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Charge import Charge













class LineItem(BaseSchema):
    #  swagger.json

    
    charges = fields.List(fields.Nested(Charge, required=False), required=False)
    
    custom_messasge = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    external_line_id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
