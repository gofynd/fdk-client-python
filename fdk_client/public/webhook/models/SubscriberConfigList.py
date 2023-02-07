"""webhook Public Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PublicModel import BaseSchema




from .SubscriberResponse import SubscriberResponse



from .Page import Page



class SubscriberConfigList(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(SubscriberResponse, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
