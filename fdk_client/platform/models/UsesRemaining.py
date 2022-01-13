"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class UsesRemaining(BaseSchema):
    # Cart swagger.json

    
    user = fields.Int(required=False)
    
    app = fields.Int(required=False)
    
    total = fields.Int(required=False)
    
