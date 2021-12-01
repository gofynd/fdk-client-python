"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .Template import Template

from .Page import Page


class TemplateGetResponse(BaseSchema):

    
    items = fields.List(fields.Nested(Template, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

