"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .UserGroupResponseSchema import UserGroupResponseSchema

from .PaginationSchema import PaginationSchema


class UserGroupListResponseSchema(BaseSchema):
    # User swagger.json

    
    items = fields.List(fields.Nested(UserGroupResponseSchema, required=False), required=False)
    
    page = fields.Nested(PaginationSchema, required=False)
    

