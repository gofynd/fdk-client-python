"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .PincodeDataResponse import PincodeDataResponse

from .PincodeErrorSchemaResponse import PincodeErrorSchemaResponse






class PincodeApiResponse(BaseSchema):
    # Logistic swagger.json

    
    stormbreaker_uuid = fields.Str(required=False)
    
    data = fields.List(fields.Nested(PincodeDataResponse, required=False), required=False)
    
    error = fields.Nested(PincodeErrorSchemaResponse, required=False)
    
    request_uuid = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    

