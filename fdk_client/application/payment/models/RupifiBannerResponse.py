"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .RupifiBannerData import RupifiBannerData





class RupifiBannerResponse(BaseSchema):
    #  swagger.json

    
    data = fields.Nested(RupifiBannerData, required=False)
    
    success = fields.Boolean(required=False)
    
