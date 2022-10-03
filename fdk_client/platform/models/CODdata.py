"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class CODdata(BaseSchema):
    # Payment swagger.json

    
    user_id = fields.Str(required=False)
    
    usages = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    limit = fields.Int(required=False)
    
    remaining_limit = fields.Int(required=False)
    

