"""billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class InvoiceDetailsClient(BaseSchema):
    #  swagger.json

    
    address_lines = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
