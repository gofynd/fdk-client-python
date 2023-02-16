"""lead Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class TicketFeedbackForm(BaseSchema):
    #  swagger.json

    
    title = fields.Str(required=False)
    
    display = fields.List(fields.Dict(required=False), required=False)
    
