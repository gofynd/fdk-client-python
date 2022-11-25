"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class UserInfo1(BaseSchema):
    # Order swagger.json

    
    gender = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    

