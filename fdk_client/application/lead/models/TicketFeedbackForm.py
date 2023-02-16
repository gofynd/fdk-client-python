"""lead Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class TicketFeedbackForm(BaseSchema):
    #  swagger.json

    
    title = fields.Str(required=False)
    
    display = fields.List(fields.Dict(required=False), required=False)
    
