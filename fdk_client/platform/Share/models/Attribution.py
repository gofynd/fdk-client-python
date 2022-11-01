"""Share Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class Attribution(BaseSchema):
    #  swagger.json

    
    campaign_cookie_expiry = fields.Str(required=False)
    
