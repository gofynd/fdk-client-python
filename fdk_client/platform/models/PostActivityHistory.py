"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PostHistoryData import PostHistoryData

from .PostHistoryFilters import PostHistoryFilters


class PostActivityHistory(BaseSchema):
    # Order swagger.json

    
    data = fields.Nested(PostHistoryData, required=False)
    
    filters = fields.List(fields.Nested(PostHistoryFilters, required=False), required=False)
    

