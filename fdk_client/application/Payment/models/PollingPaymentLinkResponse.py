"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema
























class PollingPaymentLinkResponse(BaseSchema):
    #  swagger.json

    
    amount = fields.Float(required=False)
    
    status = fields.Str(required=False)
    
    status_code = fields.Int(required=False)
    
    aggregator_name = fields.Str(required=False)
    
    redirect_url = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    payment_link_id = fields.Str(required=False)
    
    http_status = fields.Int(required=False)
    