"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class PincodeParentsResponse(BaseSchema):
    # Logistic swagger.json

    
    uid = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    

