"""communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Log import Log



from .Page import Page



class Logs(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(Log, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
