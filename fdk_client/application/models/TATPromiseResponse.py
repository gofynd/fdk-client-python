"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .TATTimestampResponse import TATTimestampResponse

from .TATFormattedResponse import TATFormattedResponse


class TATPromiseResponse(BaseSchema):
    # Logistic swagger.json

    
    timestamp = fields.Nested(TATTimestampResponse, required=False)
    
    formatted = fields.Nested(TATFormattedResponse, required=False)
    

