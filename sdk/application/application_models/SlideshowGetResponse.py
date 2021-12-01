"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .SlideshowSchema import SlideshowSchema

from .Page import Page


class SlideshowGetResponse(BaseSchema):

    
    items = fields.List(fields.Nested(SlideshowSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

