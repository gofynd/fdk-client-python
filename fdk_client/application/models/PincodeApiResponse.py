"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DataResponse import DataResponse



from .Error import Error


class PincodeApiResponse(BaseSchema):
    # Logistic swagger.json

    
    data = fields.List(fields.Nested(DataResponse, required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(Error, required=False)
    

