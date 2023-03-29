"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Dimensions import Dimensions


class Meta(BaseSchema):
    # Order swagger.json

    
    dimension = fields.Nested(Dimensions, required=False)
    

