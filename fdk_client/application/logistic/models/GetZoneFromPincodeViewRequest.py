"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class GetZoneFromPincodeViewRequest(BaseSchema):
    #  swagger.json

    
    country = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
