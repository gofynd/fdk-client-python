"""communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Campaign import Campaign



from .Page import Page



class Campaigns(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(Campaign, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
