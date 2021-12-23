"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema










class ItemTotal(BaseSchema):
    # Order swagger.json

    
    new = fields.Int(required=False)
    
    processing = fields.Int(required=False)
    
    returns = fields.Int(required=False)
    
    all = fields.Int(required=False)
    

