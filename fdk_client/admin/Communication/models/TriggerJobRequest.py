"""Communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class TriggerJobRequest(BaseSchema):
    #  swagger.json

    
    job_id = fields.Str(required=False)
    
