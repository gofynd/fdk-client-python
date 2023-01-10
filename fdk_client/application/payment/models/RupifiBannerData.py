"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class RupifiBannerData(BaseSchema):
    #  swagger.json

    
    status = fields.Str(required=False)
    
    kyc_url = fields.Str(required=False)
    
