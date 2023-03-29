"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .TATFormattedResponse import TATFormattedResponse

from .TATTimestampResponse import TATTimestampResponse


class TATPromiseResponse(BaseSchema):
    # Logistic swagger.json

    
    formatted = fields.Nested(TATFormattedResponse, required=False)
    
    timestamp = fields.Nested(TATTimestampResponse, required=False)
    

