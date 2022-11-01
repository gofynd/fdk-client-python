"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .EpaylaterBannerData import EpaylaterBannerData





class EpaylaterBannerResponse(BaseSchema):
    #  swagger.json

    
    data = fields.Nested(EpaylaterBannerData, required=False)
    
    success = fields.Boolean(required=False)
    
