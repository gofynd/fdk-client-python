"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class WalletOtpRequest(BaseSchema):
    #  swagger.json

    
    mobile = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
