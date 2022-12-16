"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class GetShareCartLinkRequest(BaseSchema):
    #  swagger.json

    
    id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    