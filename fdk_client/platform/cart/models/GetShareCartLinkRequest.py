"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class GetShareCartLinkRequest(BaseSchema):
    #  swagger.json

    
    meta = fields.Dict(required=False)
    
    id = fields.Str(required=False)
    
