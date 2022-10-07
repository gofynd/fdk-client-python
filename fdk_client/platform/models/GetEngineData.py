"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .GetEngineFilters import GetEngineFilters


class GetEngineData(BaseSchema):
    # Finance swagger.json

    
    project = fields.List(fields.Str(required=False), required=False)
    
    table_name = fields.Str(required=False)
    
    filters = fields.Nested(GetEngineFilters, required=False)
    

