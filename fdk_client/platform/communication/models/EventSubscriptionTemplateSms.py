"""communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class EventSubscriptionTemplateSms(BaseSchema):
    #  swagger.json

    
    subscribed = fields.Boolean(required=False)
    
    template = fields.Str(required=False)
    
