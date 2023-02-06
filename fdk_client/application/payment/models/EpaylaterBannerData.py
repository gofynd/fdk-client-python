"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class EpaylaterBannerData(BaseSchema):
    #  swagger.json

    
    status = fields.Str(required=False)
    
    display = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
