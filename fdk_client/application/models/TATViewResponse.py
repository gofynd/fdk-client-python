"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .TATError import TATError













from .LocationDetailsResponse import LocationDetailsResponse










class TATViewResponse(BaseSchema):
    # Logistic swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(TATError, required=False)
    
    is_cod_available = fields.Boolean(required=False)
    
    journey = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    to_pincode = fields.Str(required=False)
    
    location_details = fields.List(fields.Nested(LocationDetailsResponse, required=False), required=False)
    
    request_uuid = fields.Str(required=False)
    
    to_city = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    stormbreaker_uuid = fields.Str(required=False)
    

