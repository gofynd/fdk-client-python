"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .JsonFields import JsonFields


class ApplicationBrandJson(BaseSchema):
    # CompanyProfile swagger.json

    
    _custom_json = fields.List(fields.Nested(JsonFields, required=False), required=False)
    

