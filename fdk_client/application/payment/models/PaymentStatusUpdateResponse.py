"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class PaymentStatusUpdateResponse(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    retry = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    
    redirect_url = fields.Str(required=False)
    
    aggregator_name = fields.Str(required=False)
    