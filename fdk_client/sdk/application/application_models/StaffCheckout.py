"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema










class StaffCheckout(BaseSchema):
    # Cart swagger.json

    
    last_name = fields.Str(required=False)
    
    user = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    

