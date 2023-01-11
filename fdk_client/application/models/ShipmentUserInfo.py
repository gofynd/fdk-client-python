"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class ShipmentUserInfo(BaseSchema):
    # Order swagger.json

    
    first_name = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    

