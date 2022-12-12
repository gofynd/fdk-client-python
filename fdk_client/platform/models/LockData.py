"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class LockData(BaseSchema):
    # Order swagger.json

    
    mto = fields.Boolean(required=False)
    
    locked = fields.Boolean(required=False)
    
    lock_message = fields.Str(required=False)
    

