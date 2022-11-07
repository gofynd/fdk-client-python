"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class SetCODForUserRequest(BaseSchema):
    # Payment swagger.json

    
    merchant_user_id = fields.Str(required=False)
    
    mobileno = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    

