"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class FulfillingStore(BaseSchema):
    # Order swagger.json

    
    name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    code = fields.Str(required=False)
    
    id = fields.Int(required=False)
    

