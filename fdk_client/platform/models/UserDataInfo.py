"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




















class UserDataInfo(BaseSchema):
    # Order swagger.json

    
    email = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    avis_user_id = fields.Str(required=False)
    
    is_anonymous_user = fields.Boolean(required=False)
    
    mobile = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    gender = fields.Str(required=False)
    
    name = fields.Str(required=False)
    

