"""inventory Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .JobConfig import JobConfig



class JobConfigRawDTO(BaseSchema):
    #  swagger.json

    
    integration = fields.Str(required=False)
    
    company_name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    data = fields.Nested(JobConfig, required=False)
    
