"""companyprofile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class InvoiceCredSerializer(BaseSchema):
    #  swagger.json

    
    enabled = fields.Boolean(required=False)
    
    username = fields.Str(required=False)
    
    password = fields.Str(required=False)
    
