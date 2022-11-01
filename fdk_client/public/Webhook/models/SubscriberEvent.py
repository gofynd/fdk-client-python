"""Webhook Public Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PublicModel import BaseSchema












class SubscriberEvent(BaseSchema):
    #  swagger.json

    
    id = fields.Int(required=False)
    
    subscriber_id = fields.Int(required=False)
    
    event_id = fields.Int(required=False)
    
    created_date = fields.Str(required=False)
    
