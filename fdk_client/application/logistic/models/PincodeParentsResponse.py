"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class PincodeParentsResponse(BaseSchema):
    #  swagger.json

    
    display_name = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    