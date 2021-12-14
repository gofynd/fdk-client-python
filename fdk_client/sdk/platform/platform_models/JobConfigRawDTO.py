"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema







from .JobConfig import JobConfig


class JobConfigRawDTO(BaseSchema):
    # Inventory swagger.json

    
    integration = fields.Str(required=False)
    
    company_name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    data = fields.Nested(JobConfig, required=False)
    

