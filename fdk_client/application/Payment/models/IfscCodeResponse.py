"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class IfscCodeResponse(BaseSchema):
    #  swagger.json

    
    bank_name = fields.Str(required=False)
    
    branch_name = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    