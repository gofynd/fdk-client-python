"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class ValidateCustomerResponse(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    error = fields.Dict(required=False)
    
    success = fields.Boolean(required=False)
    
    data = fields.Dict(required=False)
    
