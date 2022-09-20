"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema















from .TATErrorSchemaResponse import TATErrorSchemaResponse







from .TATLocationDetailsResponse import TATLocationDetailsResponse




class TATViewResponse(BaseSchema):
    # Logistic swagger.json

    
    journey = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    to_pincode = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    to_city = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    request_uuid = fields.Str(required=False)
    
    error = fields.Nested(TATErrorSchemaResponse, required=False)
    
    success = fields.Boolean(required=False)
    
    identifier = fields.Str(required=False)
    
    is_cod_available = fields.Boolean(required=False)
    
    location_details = fields.List(fields.Nested(TATLocationDetailsResponse, required=False), required=False)
    
    stormbreaker_uuid = fields.Str(required=False)
    

