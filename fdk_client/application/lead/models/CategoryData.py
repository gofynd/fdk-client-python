"""lead Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .TicketCategory import TicketCategory



class CategoryData(BaseSchema):
    #  swagger.json

    
    list = fields.Nested(TicketCategory, required=False)
    
