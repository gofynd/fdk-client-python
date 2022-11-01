"""Communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .EventSubscriptionTemplateSms import EventSubscriptionTemplateSms



from .EventSubscriptionTemplateEmail import EventSubscriptionTemplateEmail



class EventSubscriptionTemplate(BaseSchema):
    #  swagger.json

    
    sms = fields.Nested(EventSubscriptionTemplateSms, required=False)
    
    email = fields.Nested(EventSubscriptionTemplateEmail, required=False)
    
