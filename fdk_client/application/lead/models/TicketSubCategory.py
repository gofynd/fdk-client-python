"""lead Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class TicketSubCategory(BaseSchema):
    #  swagger.json

    
    key = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    sub_categories = fields.Nested(lambda: TicketSubCategory(exclude=('sub_categories')), required=False)
    
