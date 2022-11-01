"""Configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ApplicationVersionRequest import ApplicationVersionRequest



from .Device import Device







class AppVersionRequest(BaseSchema):
    #  swagger.json

    
    application = fields.Nested(ApplicationVersionRequest, required=False)
    
    device = fields.Nested(Device, required=False)
    
    locale = fields.Str(required=False)
    
    timezone = fields.Str(required=False)
    
