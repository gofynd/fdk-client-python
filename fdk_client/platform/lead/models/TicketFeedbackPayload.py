"""lead Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class TicketFeedbackPayload(BaseSchema):
    #  swagger.json

    
    form_response = fields.Dict(required=False)
    
