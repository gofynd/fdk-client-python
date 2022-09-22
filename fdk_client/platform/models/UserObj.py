"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




















class UserObj(BaseSchema):
    # Order swagger.json

    
    u_id = fields.Int(required=False)
    
    mobile = fields.Str(required=False)
    
    is_anonymous_user = fields.Boolean(required=False)
    
    last_name = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    user_oid = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    mongo_user_id = fields.Str(required=False)
    

