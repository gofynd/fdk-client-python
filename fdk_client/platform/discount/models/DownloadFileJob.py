"""discount Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class DownloadFileJob(BaseSchema):
    #  swagger.json

    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
