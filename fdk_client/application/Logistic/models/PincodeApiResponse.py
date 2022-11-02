"""Logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .PincodeDataResponse import PincodeDataResponse





from .PincodeErrorSchemaResponse import PincodeErrorSchemaResponse



class PincodeApiResponse(BaseSchema):
    #  swagger.json

    
    data = fields.List(fields.Nested(PincodeDataResponse, required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(PincodeErrorSchemaResponse, required=False)
    