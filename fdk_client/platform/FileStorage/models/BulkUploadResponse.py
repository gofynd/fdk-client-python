"""FileStorage Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .CopyFileTask import CopyFileTask



class BulkUploadResponse(BaseSchema):
    #  swagger.json

    
    tracking_url = fields.Str(required=False)
    
    task = fields.Nested(CopyFileTask, required=False)
    
