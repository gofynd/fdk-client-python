"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema







from .LogisticPincodeData import LogisticPincodeData


class GetPincodeCityResponse(BaseSchema):

    
    request_uuid = fields.Str(required=False)
    
    stormbreaker_uuid = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    data = fields.List(fields.Nested(LogisticPincodeData, required=False), required=False)
    

