"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class PaymentStatusUpdateResponse(BaseSchema):
    #  swagger.json

    
    aggregator_name = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    retry = fields.Boolean(required=False)
    
    redirect_url = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
