"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class EntitiesReasons(BaseSchema):
    # Order swagger.json

    
    data = fields.Dict(required=False)
    
    filters = fields.List(fields.Dict(required=False), required=False)
    

