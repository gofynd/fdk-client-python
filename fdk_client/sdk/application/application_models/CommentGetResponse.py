"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .Comment import Comment

from .Page import Page


class CommentGetResponse(BaseSchema):
    # Feedback swagger.json

    
    items = fields.List(fields.Nested(Comment, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

