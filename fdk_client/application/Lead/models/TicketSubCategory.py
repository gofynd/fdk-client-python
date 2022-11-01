"""Lead Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class TicketSubCategory(BaseSchema):
    #  swagger.json

    
    key = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
