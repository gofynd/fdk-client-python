"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class ApplicationCategoryJson(BaseSchema):
    #  swagger.json

    
    _custom_json = fields.Dict(required=False)
    
