"""payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class IfscCodeResponse(BaseSchema):
    #  swagger.json

    
    bank_name = fields.Str(required=False)
    
    branch_name = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
