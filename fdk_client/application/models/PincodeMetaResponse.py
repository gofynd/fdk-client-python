"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class PincodeMetaResponse(BaseSchema):
    # Logistic swagger.json

    
    zone = fields.Str(required=False)
    
    internal_zone_id = fields.Int(required=False)
    

