"""Communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class MetaStructure(BaseSchema):
    #  swagger.json

    
    job_type = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    trace = fields.Str(required=False)
    
    timestamp = fields.Str(required=False)
    
