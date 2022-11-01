"""Lead Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class TicketFeedbackPayload(BaseSchema):
    #  swagger.json

    
    form_response = fields.Dict(required=False)
    
