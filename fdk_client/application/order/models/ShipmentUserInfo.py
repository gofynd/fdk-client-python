"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class ShipmentUserInfo(BaseSchema):
    #  swagger.json

    
    mobile = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
