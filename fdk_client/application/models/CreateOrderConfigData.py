"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CreateOrderConfig import CreateOrderConfig


class CreateOrderConfigData(BaseSchema):
    # Order swagger.json

    
    config_data = fields.Nested(CreateOrderConfig, required=False)
    

