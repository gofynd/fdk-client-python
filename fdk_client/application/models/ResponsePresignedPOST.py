"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class ResponsePresignedPOST(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    method = fields.Str(required=False)
    
    event = fields.Str(required=False)
    
    payload = fields.List(fields.Raw(required=False), required=False)
    

