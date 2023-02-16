"""communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






















class CampaignReq(BaseSchema):
    #  swagger.json

    
    description = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    headers = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    file_url = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    records_count = fields.Int(required=False)
    
    application = fields.Str(required=False)
    
