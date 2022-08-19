"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




















class UserObj(BaseSchema):
    # Order swagger.json

    
    first_name = fields.Str(required=False)
    
    mongo_user_id = fields.Str(required=False)
    
    u_id = fields.Int(required=False)
    
    email = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    user_oid = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    is_anonymous_user = fields.Boolean(required=False)
    

