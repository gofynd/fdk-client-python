"""lead Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Ticket import Ticket



from .Filter import Filter



from .Page import Page



class TicketList(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(Ticket, required=False), required=False)
    
    filters = fields.Nested(Filter, required=False)
    
    page = fields.Nested(Page, required=False)
    
