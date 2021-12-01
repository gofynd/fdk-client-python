"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema










class BulkProductRequest(BaseSchema):

    
    batch_id = fields.Str(required=False)
    
    template_tag = fields.Str(required=False)
    
    data = fields.List(fields.Dict(required=False), required=False)
    
    company_id = fields.Int(required=False)
    

