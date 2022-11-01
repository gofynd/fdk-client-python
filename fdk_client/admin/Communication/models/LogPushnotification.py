"""Communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class LogPushnotification(BaseSchema):
    #  swagger.json

    
    pushtokens = fields.List(fields.Str(required=False), required=False)
    
