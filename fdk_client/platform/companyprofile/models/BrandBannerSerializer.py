"""companyprofile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class BrandBannerSerializer(BaseSchema):
    #  swagger.json

    
    portrait = fields.Str(required=False)
    
    landscape = fields.Str(required=False)
    