"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema







from .ChildrenSchema import ChildrenSchema












class FAQCategorySchema(BaseSchema):

    
    index = fields.Int(required=False)
    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    children = fields.List(fields.Nested(ChildrenSchema, required=False), required=False)
    
    _id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    icon_url = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    

