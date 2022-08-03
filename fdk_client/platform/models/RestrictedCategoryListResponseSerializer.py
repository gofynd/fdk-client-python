"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Page import Page

from .RestrictedCategoryResponseSerializer import RestrictedCategoryResponseSerializer




class RestrictedCategoryListResponseSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(RestrictedCategoryResponseSerializer, required=False), required=False)
    
    declaration_template = fields.Dict(required=False)
    

