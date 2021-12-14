"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class GeoLoc(BaseSchema):
    # Feedback swagger.json

    
    latitude = fields.Str(required=False)
    
    longitude = fields.Str(required=False)
    

