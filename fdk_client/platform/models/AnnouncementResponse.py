"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






















class AnnouncementResponse(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False)
    
    platform_id = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    platform_name = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    from_datetime = fields.Str(required=False)
    
    to_datetime = fields.Str(required=False)
    
    logo_url = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    

