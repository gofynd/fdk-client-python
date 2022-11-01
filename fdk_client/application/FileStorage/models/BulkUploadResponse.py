"""FileStorage Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .CopyFileTask import CopyFileTask



class BulkUploadResponse(BaseSchema):
    #  swagger.json

    
    tracking_url = fields.Str(required=False)
    
    task = fields.Nested(CopyFileTask, required=False)
    
