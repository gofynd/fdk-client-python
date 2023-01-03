"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class CancelPaymentLinkResponse(BaseSchema):
    #  swagger.json

    
    status_code = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
