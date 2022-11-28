"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .StatusesBody import StatusesBody


class ShipmentApplicationStatusResponse(BaseSchema):
    # Order swagger.json

    
    statuses = fields.List(fields.Nested(StatusesBody, required=False), required=False)
    

