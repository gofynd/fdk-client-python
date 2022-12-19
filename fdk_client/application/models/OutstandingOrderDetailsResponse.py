"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class OutstandingOrderDetailsResponse(BaseSchema):
    # Payment swagger.json

    
    status_code = fields.Int(required=False)
    
    data = fields.List(fields.Dict(required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    

