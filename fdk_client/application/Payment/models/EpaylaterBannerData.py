"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class EpaylaterBannerData(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    display = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    
