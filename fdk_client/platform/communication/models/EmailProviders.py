"""communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .EmailProvider import EmailProvider



from .Page import Page



class EmailProviders(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(EmailProvider, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
