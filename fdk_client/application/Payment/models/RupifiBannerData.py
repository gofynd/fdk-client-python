"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class RupifiBannerData(BaseSchema):
    #  swagger.json

    
    kyc_url = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
