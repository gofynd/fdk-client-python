"""webhook Public Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PublicModel import BaseSchema




from .EventConfig import EventConfig



from .Page import Page



class EventConfigList(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(EventConfig, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
