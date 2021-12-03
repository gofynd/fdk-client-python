"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .UserSchema import UserSchema


class UserSearchResponseSchema(BaseSchema):

    
    users = fields.List(fields.Nested(UserSchema, required=False), required=False)
    

