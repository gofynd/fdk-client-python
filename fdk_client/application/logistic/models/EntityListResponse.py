"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .PincodeEntityResponse import PincodeEntityResponse



class EntityListResponse(BaseSchema):
    #  swagger.json

    
    count = fields.Int(required=False)
    
    results = fields.List(fields.Nested(PincodeEntityResponse, required=False), required=False)
    
