"""communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Audience import Audience



from .Page import Page



class Audiences(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(Audience, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
