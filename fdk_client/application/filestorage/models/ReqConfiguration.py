"""filestorage Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class ReqConfiguration(BaseSchema):
    #  swagger.json

    
    concurrency = fields.Int(required=False)
    
