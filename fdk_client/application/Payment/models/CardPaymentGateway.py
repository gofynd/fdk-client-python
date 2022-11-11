"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class CardPaymentGateway(BaseSchema):
    #  swagger.json

    
    customer_id = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    api = fields.Str(required=False)
    
