"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class GetShareCartLinkRequest(BaseSchema):
    #  swagger.json

    
    meta = fields.Dict(required=False)
    
    id = fields.Str(required=False)
    
