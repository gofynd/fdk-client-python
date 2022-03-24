"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ZoneRequest(BaseSchema):
    # Serviceability swagger.json

    
    data = fields.Dict(required=False)
    
    channels = fields.List(fields.Dict(required=False), required=False)
    
    identifier = fields.Str(required=False)
    

