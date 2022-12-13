"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .HistoryDict import HistoryDict


class ShipmentHistoryResponse(BaseSchema):
    # Order swagger.json

    
    activity_history = fields.List(fields.Nested(HistoryDict, required=False), required=False)
    

