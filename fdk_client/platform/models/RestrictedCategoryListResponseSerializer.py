"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .RestrictedCategoryResponseSerializer import RestrictedCategoryResponseSerializer

from .Page import Page




class RestrictedCategoryListResponseSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    items = fields.List(fields.Nested(RestrictedCategoryResponseSerializer, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    declaration_template = fields.Dict(required=False)
    

