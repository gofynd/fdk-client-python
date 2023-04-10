"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PostActivityHistory import PostActivityHistory


class PostHistoryDict(BaseSchema):
    # Order swagger.json

    
    activity_history = fields.Nested(PostActivityHistory, required=False)
    

