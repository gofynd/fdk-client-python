"""billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .InvoicesData import InvoicesData













class Invoices(BaseSchema):
    #  swagger.json

    
    data = fields.List(fields.Nested(InvoicesData, required=False), required=False)
    
    start = fields.Int(required=False)
    
    end = fields.Int(required=False)
    
    limit = fields.Int(required=False)
    
    page = fields.Int(required=False)
    
    total = fields.Int(required=False)
    
