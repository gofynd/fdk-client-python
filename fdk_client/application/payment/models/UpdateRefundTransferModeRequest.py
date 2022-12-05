"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class UpdateRefundTransferModeRequest(BaseSchema):
    #  swagger.json

    
    transfer_mode = fields.Str(required=False)
    
    enable = fields.Boolean(required=False)
    
