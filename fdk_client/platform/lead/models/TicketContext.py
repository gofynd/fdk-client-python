"""lead Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class TicketContext(BaseSchema):
    #  swagger.json

    
    application_id = fields.Str(required=False)
    
    company_id = fields.Str(required=False)
    
