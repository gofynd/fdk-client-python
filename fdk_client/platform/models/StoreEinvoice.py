"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class StoreEinvoice(BaseSchema):
    # Orders swagger.json

    
    enabled = fields.Boolean(required=False)
    
    user = fields.Str(required=False)
    
    username = fields.Str(required=False)
    
    password = fields.Str(required=False)
    
