"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AllSizes import AllSizes


class ListALLSizes(BaseSchema):
    # Catalog swagger.json

    
    all_sizes = fields.List(fields.Nested(AllSizes, required=False), required=False)
    

