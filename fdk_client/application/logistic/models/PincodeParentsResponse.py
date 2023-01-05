"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class PincodeParentsResponse(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
