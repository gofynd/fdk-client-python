"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class OrderCommitted(BaseSchema):

    
    count = fields.Int(required=False)
    
    updated_at = fields.Str(required=False)
    

