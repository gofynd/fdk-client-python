"""Communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class TriggerJobResponse(BaseSchema):
    #  swagger.json

    
    status = fields.Int(required=False)
    
