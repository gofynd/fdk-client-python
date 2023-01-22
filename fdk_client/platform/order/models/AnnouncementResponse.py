"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
























class AnnouncementResponse(BaseSchema):
    #  swagger.json

    
    title = fields.Str(required=False)
    
    platform_name = fields.Str(required=False)
    
    to_datetime = fields.Str(required=False)
    
    platform_id = fields.Str(required=False)
    
    logo_url = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    from_datetime = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    