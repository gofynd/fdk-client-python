"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .PageSchema import PageSchema

from .Page import Page


class PageGetResponse(BaseSchema):

    
    items = fields.List(fields.Nested(PageSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

