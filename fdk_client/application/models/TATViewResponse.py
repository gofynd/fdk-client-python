"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .TATLocationDetailsResponse import TATLocationDetailsResponse













from .TATErrorSchemaResponse import TATErrorSchemaResponse






class TATViewResponse(BaseSchema):
    # Logistic swagger.json

    
    to_pincode = fields.Str(required=False)
    
    request_uuid = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    location_details = fields.List(fields.Nested(TATLocationDetailsResponse, required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    action = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    journey = fields.Str(required=False)
    
    stormbreaker_uuid = fields.Str(required=False)
    
    is_cod_available = fields.Boolean(required=False)
    
    error = fields.Nested(TATErrorSchemaResponse, required=False)
    
    identifier = fields.Str(required=False)
    
    to_city = fields.Str(required=False)
    

