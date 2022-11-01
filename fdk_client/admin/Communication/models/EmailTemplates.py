"""Communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .EmailTemplate import EmailTemplate



from .Page import Page



class EmailTemplates(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(EmailTemplate, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
