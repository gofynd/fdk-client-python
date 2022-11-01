"""Partner Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




















class AddProxyResponse(BaseSchema):
    #  swagger.json

    
    _id = fields.Str(required=False)
    
    attached_path = fields.Str(required=False)
    
    proxy_url = fields.Str(required=False)
    
    company_id = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    extension_id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
