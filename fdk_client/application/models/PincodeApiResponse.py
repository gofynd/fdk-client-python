"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .PincodeErrorSchemaResponse import PincodeErrorSchemaResponse

from .PincodeDataResponse import PincodeDataResponse


class PincodeApiResponse(BaseSchema):
    # Logistic swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(PincodeErrorSchemaResponse, required=False)
    
    data = fields.List(fields.Nested(PincodeDataResponse, required=False), required=False)
    

