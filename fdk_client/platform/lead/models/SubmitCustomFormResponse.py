"""lead Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .Ticket import Ticket



class SubmitCustomFormResponse(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    ticket = fields.Nested(Ticket, required=False)
    
