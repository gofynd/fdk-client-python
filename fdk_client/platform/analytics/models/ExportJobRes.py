"""analytics Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class ExportJobRes(BaseSchema):
    #  swagger.json

    
    status = fields.Str(required=False)
    
    job_id = fields.Str(required=False)
    
