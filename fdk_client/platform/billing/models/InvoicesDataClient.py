"""billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class InvoicesDataClient(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    address_lines = fields.List(fields.Str(required=False), required=False)
    
