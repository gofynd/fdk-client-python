"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .createOrderConfigResponse import createOrderConfigResponse


class CreateOrderConfigDataResponse(BaseSchema):
    # Order swagger.json

    
    data = fields.List(fields.Nested(createOrderConfigResponse, required=False), required=False)
    

