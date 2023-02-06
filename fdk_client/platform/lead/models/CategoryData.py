"""lead Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .TicketCategory import TicketCategory



class CategoryData(BaseSchema):
    #  swagger.json

    
    list = fields.Nested(TicketCategory, required=False)
    
