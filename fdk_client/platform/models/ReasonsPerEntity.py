"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ReasonText import ReasonText


class ReasonsPerEntity(BaseSchema):
    # Order swagger.json

    
    entity_key = fields.Nested(ReasonText, required=False)
    

