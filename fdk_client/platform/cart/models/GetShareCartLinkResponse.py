"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class GetShareCartLinkResponse(BaseSchema):
    #  swagger.json

    
    share_url = fields.Str(required=False)
    
    token = fields.Str(required=False)
    
