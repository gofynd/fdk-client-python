"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .EdcModelData import EdcModelData




class EdcAggregatorAndModelListResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.List(fields.Nested(EdcModelData, required=False), required=False)
    
    success = fields.Boolean(required=False)
    

