"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ReasonsPerEntity import ReasonsPerEntity


class EntityReason(BaseSchema):
    # Order swagger.json

    
    bag_ids = fields.Nested(ReasonsPerEntity, required=False)
    

