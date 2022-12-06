"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class GetShareCartLinkResponse(BaseSchema):
    #  swagger.json

    
    share_url = fields.Str(required=False)
    
    token = fields.Str(required=False)
    
