"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class StaffCheckout(BaseSchema):
    #  swagger.json

    
    first_name = fields.Str(required=False)
    
    user = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
