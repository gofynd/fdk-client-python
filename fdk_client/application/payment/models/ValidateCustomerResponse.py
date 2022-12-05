"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class ValidateCustomerResponse(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.Dict(required=False)
    
    data = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    
