"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class EInvoicePortalDetails(BaseSchema):
    #  swagger.json

    
    username = fields.Str(required=False)
    
    user = fields.Str(required=False)
    
    password = fields.Str(required=False)
    
