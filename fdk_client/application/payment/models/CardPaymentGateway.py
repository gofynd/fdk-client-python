"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class CardPaymentGateway(BaseSchema):
    #  swagger.json

    
    api = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    customer_id = fields.Str(required=False)
    
