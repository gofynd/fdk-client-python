"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class GetShareCartLinkResponse(BaseSchema):
    #  swagger.json

    
    token = fields.Str(required=False)
    
    share_url = fields.Str(required=False)
    
