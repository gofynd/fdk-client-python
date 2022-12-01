"""filestorage Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class ReqConfiguration(BaseSchema):
    #  swagger.json

    
    concurrency = fields.Int(required=False)
    
