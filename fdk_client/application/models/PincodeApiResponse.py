"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PincodeErrorSchemaResponse import PincodeErrorSchemaResponse



from .PincodeDataResponse import PincodeDataResponse


class PincodeApiResponse(BaseSchema):
    # Logistic swagger.json

    
    error = fields.Nested(PincodeErrorSchemaResponse, required=False)
    
    success = fields.Boolean(required=False)
    
    data = fields.List(fields.Nested(PincodeDataResponse, required=False), required=False)
    

