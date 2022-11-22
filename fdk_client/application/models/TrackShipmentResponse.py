"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .TrackShipmentResults import TrackShipmentResults


class TrackShipmentResponse(BaseSchema):
    # Order swagger.json

    
    results = fields.List(fields.Nested(TrackShipmentResults, required=False), required=False)
    

