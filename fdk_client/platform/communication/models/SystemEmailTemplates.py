"""communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .SystemEmailTemplate import SystemEmailTemplate



from .Page import Page



class SystemEmailTemplates(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(SystemEmailTemplate, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
