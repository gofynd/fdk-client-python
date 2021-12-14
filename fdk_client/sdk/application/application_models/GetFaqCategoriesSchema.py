"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .CategorySchema import CategorySchema


class GetFaqCategoriesSchema(BaseSchema):
    # Content swagger.json

    
    categories = fields.List(fields.Nested(CategorySchema, required=False), required=False)
    

