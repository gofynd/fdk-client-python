"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class Products(BaseSchema):
    #  swagger.json

    
    line_number = fields.Int(required=False)
    
    identifier = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
