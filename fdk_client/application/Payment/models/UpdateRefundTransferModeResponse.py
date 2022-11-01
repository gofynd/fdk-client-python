"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class UpdateRefundTransferModeResponse(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
