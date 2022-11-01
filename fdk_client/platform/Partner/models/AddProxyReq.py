"""Partner Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class AddProxyReq(BaseSchema):
    #  swagger.json

    
    attached_path = fields.Str(required=False)
    
    proxy_url = fields.Str(required=False)
    
