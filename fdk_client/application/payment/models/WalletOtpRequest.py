"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class WalletOtpRequest(BaseSchema):
    #  swagger.json

    
    country_code = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
