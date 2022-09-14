"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Error import Error

from .DataResponse import DataResponse




class PincodeApiResponse(BaseSchema):
    # Logistic swagger.json

    
    error = fields.Nested(Error, required=False)
    
    data = fields.List(fields.Nested(DataResponse, required=False), required=False)
    
    success = fields.Boolean(required=False)
    

