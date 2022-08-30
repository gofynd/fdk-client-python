"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class StoreEinvoice(BaseSchema):
    # Order swagger.json

    
    password = fields.Str(required=False)
    
    enabled = fields.Boolean(required=False)
    
    user = fields.Str(required=False)
    
    username = fields.Str(required=False)
    

