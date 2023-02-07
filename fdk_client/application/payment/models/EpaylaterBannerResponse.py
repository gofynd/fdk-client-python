"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .EpaylaterBannerData import EpaylaterBannerData



class EpaylaterBannerResponse(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(EpaylaterBannerData, required=False)
    
