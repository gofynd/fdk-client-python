"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class UserDataSet(BaseSchema):
    # Orders swagger.json

    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    mobile = fields.Int(required=False)
    

