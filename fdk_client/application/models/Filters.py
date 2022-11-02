"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Statuses import Statuses


class Filters(BaseSchema):
    # Order swagger.json

    
    statuses = fields.List(fields.Nested(Statuses, required=False), required=False)
    

