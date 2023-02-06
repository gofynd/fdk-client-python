"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .PincodeErrorSchemaResponse import PincodeErrorSchemaResponse





from .PincodeDataResponse import PincodeDataResponse



class PincodeApiResponse(BaseSchema):
    #  swagger.json

    
    error = fields.Nested(PincodeErrorSchemaResponse, required=False)
    
    success = fields.Boolean(required=False)
    
    data = fields.List(fields.Nested(PincodeDataResponse, required=False), required=False)
    
