"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema


















class KYCAddress(BaseSchema):
    #  swagger.json

    
    addressline1 = fields.Str(required=False)
    
    land_mark = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    ownership_type = fields.Str(required=False)
    
    addressline2 = fields.Str(required=False)
    
    state = fields.Str(required=False)
    