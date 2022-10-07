"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .GetReason import GetReason


class GetReasonRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(GetReason, required=False)
    

