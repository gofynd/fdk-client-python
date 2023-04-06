"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class UpdateUserCartMapping(BaseSchema):
    # Cart swagger.json

    
    user_id = fields.Str(required=False)
    

