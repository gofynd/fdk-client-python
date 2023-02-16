"""lead Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .Ticket import Ticket



class SubmitCustomFormResponse(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    ticket = fields.Nested(Ticket, required=False)
    
